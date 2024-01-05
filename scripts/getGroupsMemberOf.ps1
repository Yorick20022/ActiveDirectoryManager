param (
    [string]$adUser
)

Get-ADPrincipalGroupMembership $adUser | Select-Object name
