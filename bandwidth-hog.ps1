Write-Output "Starting bandwidth monitoring..."
$csvOutput = ".\data\$env:computername.csv" # Output path for the csv
{} | Select-Object "Hostname", #
                   "NIC1", "BandwidthNIC1", 
                   "NIC2", "BandwidthNIC2",
                   "NIC3", "BandwidthNIC3",
                   "NIC4", "BandwidthNIC4",
                   "NIC5", "BandwidthNIC5",
                   "NIC6", "BandwidthNIC6",
                   "NIC7", "BandwidthNIC7",
                   "NIC8", "BandwidthNIC8", 
                   "Time", "Date" | Export-Csv $csvOutput # Creates a blank csv header to append the data to
$counter = 0 # Counter for iteration
$csvLoad = Import-Csv $csvOutput # Loads the csv into the script
do {
    # Below function takes gets the CimInstance object and snapshots the data we need
    $bandwidthQuery = Get-CimInstance -Query "Select BytesTotalPersec from Win32_PerfFormattedData_Tcpip_NetworkInterface" | Select-Object -Property Name, BytesTotalPerSec
    $csvLoad.Hostname = $env:computername

    $csvLoad.NIC1 = $bandwidthQuery[0].Name # Puts the name of the first NIC into the column
    $bytes = $bandwidthQuery[0].BytesTotalPerSec #  # Gets the bytes per second of the NIC and places it in a variable 
    $csvLoad.BandwidthNIC1 = [math]::Round($bytes / (1024 * 1024), 2) # Converts the traffic coming through the NIC to MB and rounds it to 2 decimal places

    $csvLoad.NIC2 = $bandwidthQuery[1].Name # 
    $bytes = $bandwidthQuery[1].BytesTotalPerSec
    $csvLoad.BandwidthNIC2 = [math]::Round($bytes / (1024 * 1024), 2)

    $csvLoad.NIC3 = $bandwidthQuery[2].Name
    $bytes = $bandwidthQuery[2].BytesTotalPerSec
    $csvLoad.BandwidthNIC3 = [math]::Round($bytes / (1024 * 1024), 2)

    $csvLoad.NIC4 = $bandwidthQuery[3].Name
    $bytes = $bandwidthQuery[3].BytesTotalPerSec
    $csvLoad.BandwidthNIC4 = [math]::Round($bytes / (1024 * 1024), 2)

    $csvLoad.NIC5 = $bandwidthQuery[4].Name
    $bytes = $bandwidthQuery[4].BytesTotalPerSec
    $csvLoad.BandwidthNIC5 = [math]::Round($bytes / (1024 * 1024), 2)

    $csvLoad.NIC6 = $bandwidthQuery[5].Name
    $bytes = $bandwidthQuery[5].BytesTotalPerSec
    $csvLoad.BandwidthNIC6 = [math]::Round($bytes / (1024 * 1024), 2)

    $csvLoad.NIC7 = $bandwidthQuery[6].Name
    $bytes = $bandwidthQuery[6].BytesTotalPerSec
    $csvLoad.BandwidthNIC7 = [math]::Round($bytes / (1024 * 1024), 2)

    $csvLoad.NIC8 = $bandwidthQuery[7].Name
    $bytes = $bandwidthQuery[7].BytesTotalPerSec
    $csvLoad.BandwidthNIC8 = [math]::Round($bytes / (1024 * 1024), 2)

    $csvLoad.Time = $counter # Puts the counter into its own column... not an exact measure of time
    $csvLoad.Date = Get-Date -Format G
    $csvLoad | Export-Csv $csvOutput -Append # Adds this pass into the last row in the csv
    $counter++ # Counter up by 1   
    Write-Output $bandwidthQuery
    Write-Output "Running..."
} while ($counter -le 345000) # Preform the above process again until we get n data points. This is roughly a day. 
Write-Output "Done! You may eject the USB now."
# This will take a while... 