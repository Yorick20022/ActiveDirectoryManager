param (
    [string]$adUser
)

# Get the current date and time
$currentDate = Get-Date

# Replace 'pwdLastSetValue' with the actual value of pwdLastSet for the user
$pwdLastSetValue = (Get-ADUser -Identity $adUser -Properties pwdLastSet).pwdLastSet

# Convert the pwdLastSet value to a DateTime object
$pwdLastSetDateTime = [DateTime]::FromFileTime($pwdLastSetValue)

# Calculate the difference in days
$daysDifference = ($currentDate - $pwdLastSetDateTime).Days

$maxPassAge = Get-ADDefaultDomainPasswordPolicy | Select-Object -ExpandProperty MaxPasswordAge
$totalDays = [regex]::Match($maxPassAge.Days.ToString(), '\d+').Value

# Check the value of "Password never expires" attribute
$passwordNeverExpires = $adUser.PasswordNeverExpires

if ($daysDifference -eq $totalDays) { 
    Write-Host "Password change required"
}
elseif ($daysDifference -gt $totalDays) {
    Write-Host "Password change required (more than" $totalDays "days)"
}
elseif ($passwordNeverExpires) {
    "Password for $adUser never expires"
}
else {
    $remainingDays = $totalDays - $daysDifference
    Write-Host "Password change not required yet. Remaining days: $remainingDays"
}