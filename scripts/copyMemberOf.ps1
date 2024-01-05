param (
    [string]$existingUser,
    [string]$newUser
)

# Get the groups of the source user
$sourceGroups = Get-ADUser $existingUser -Properties MemberOf | Select-Object -ExpandProperty MemberOf

# Add the source user's group memberships to the target user
foreach ($group in $sourceGroups) {
    Add-ADGroupMember -Identity $group -Members $newUser
}

Write-Host "Group memberships copied from $existingUser to $newUser successfully."

