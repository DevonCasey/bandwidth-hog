$csvOutput = "$env:computername.csv" # output path for the csv
{} | Select-Object "Hostname", "NIC", "Bandwidth", "Time" | Export-Csv $csvOutput # creates a blank csv header to append the data to
$counter = 0 # counter for iteration
$csvLoad = Import-Csv $csvOutput # loads the csv into the script
do {
    # below function takes gets the CimInstance object and snapshots the data we need
    $bandwidthQuery = Get-CimInstance -Query "Select BytesTotalPersec from Win32_PerfFormattedData_Tcpip_NetworkInterface" | Select-Object -Property Name, BytesTotalPerSec
    $csvLoad.Hostname = $env:computername
    $csvLoad.NIC = $bandwidthQuery.Name # puts the name of the object into the name column of the csv
    $csvLoad.Bandwidth = [math]::Round(($bandwidthQuery.BytesTotalPerSec / 1Mb), 1) # same thing as above, but with some math to convert bytes to megabytes
    $csvLoad.Time = $counter # puts the counter into its own column... not an exact measure of time
    $csvLoad | Export-Csv $csvOutput -Append # adds this pass into the last row in the csv
    $counter++ # counter up by 1
} while ($counter -le 500) # preform the above process again until we get n data points