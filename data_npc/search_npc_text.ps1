# Ask for user input
$targetWord = Read-Host "Please input target word"
# targetWord variable now holds the user input string

# assumes target directory is npc_text, the folder itself which is in the same DIR as this program
$inputDirectory = ".\npc_text"
# use string interpolation to add the search term at the start
$outputFile = ".\$($targetWord)_results.txt"

# Initialize the output file
# Clear-Content -Path $outputFile

# Get all .txt files in the input directory with Get-ChildItem, filter flag lets you target all files ending in .txt
    # iterate over the files with a ForEach-Object loop
Get-ChildItem -Path $inputDirectory -Filter *.txt | ForEach-Object {
    $file = $_.FullName
    $fileName = $_.Name
    # knowing the pattern is name_word_salad.txt, get the NPC name from the file
    $name = $fileName -replace '_word_salad.txt', ''

    # Read the textfile's content (done per each iteration now that we're in the loop)
    $content = Get-Content -Raw -Path $file
    
    # match chars before and after the target
    $pattern = ".{0,40}" + [regex]::Escape($targetWord) + ".{0,90}"
    # save regex match to a var.
    $matches = [regex]::Matches($content, $pattern)
    
    # Write the matches to the output file
    $matches | ForEach-Object { 
        "$($name), target: $($targetWord)" | Out-File -FilePath $outputFile -Append
        $_.Value | Out-File -FilePath $outputFile -Append
    }
}

Write-Host "Search complete. Results saved to $outputFile"
Write-Host "Procees seems successful"
