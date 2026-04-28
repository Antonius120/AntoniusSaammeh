$f = 'd:\last smestet\ai based lab8\portfolio\index.html'
$lines = [System.IO.File]::ReadAllLines($f)
$newlines = New-Object System.Collections.ArrayList
for ($i = 0; $i -lt $lines.Length; $i++) {
    if ($i -lt 356 -or $i -ge 439) {
        [void]$newlines.Add($lines[$i])
    }
}
[System.IO.File]::WriteAllLines($f, $newlines)
Write-Host "Done. Removed lines 357-440."
