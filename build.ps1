# LaTeX Build Script for OTPOCMRRTBHL
# Usage: ./build.ps1 or press Ctrl+Shift+B in VS Code (after configuration)

Write-Host "🔨 Starting LaTeX build with latexmk..." -ForegroundColor Cyan

# Navigate to project directory
Push-Location $PSScriptRoot

# Clean previous build (optional)
Write-Host "🧹 Cleaning old build artifacts..." -ForegroundColor Yellow
latexmk -C | Out-Null

# Build with latexmk
Write-Host "📖 Building PDF..." -ForegroundColor Cyan
latexmk -pdf main.tex

# Check result
if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ Build completed successfully!" -ForegroundColor Green
    Write-Host "📄 Output: main.pdf (12 pages)" -ForegroundColor Green
} else {
    Write-Host "❌ Build failed. Check main.log for errors." -ForegroundColor Red
}

Pop-Location
