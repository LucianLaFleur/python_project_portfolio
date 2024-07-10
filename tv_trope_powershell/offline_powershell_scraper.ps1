# Define the input and output files
$inputFile = ".\test_denton.txt"
$outputFile = ".\virus_from_denton.txt"

# Read the entire content of the file
$content = Get-Content -Raw -Path $inputFile

# Define the regex pattern to look for "virus"
$pattern = ".{0,80}virus.{0,150}"

# Find all matches
$matches = [regex]::Matches($content, $pattern)

# Write the matches to the output file
$matches | ForEach-Object { $_.Value } | Out-File -FilePath $outputFile