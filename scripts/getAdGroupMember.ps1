param (
    [string]$adGroupName
)

Get-ADGroupMember -Identity $adGroupName | Select-Object name, SamAccountName
