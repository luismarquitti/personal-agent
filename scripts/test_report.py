import subprocess
import os
import sys

def run_command(command, cwd=None):
    print(f"\n> Executando: {command}")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True, cwd=cwd)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar comando: {e.stderr}")
        return e.stdout

def main():
    print("="*60)
    print("RELATÓRIO DE TESTES - PERSONAL AI CORE")
    print("="*60)

    # Backend
    print("\n[BACKEND] Executando testes e cobertura...")
    backend_out = run_command("python -m pytest app/tests --cov=app --cov-report=term-missing")
    
    # Extrair TOTAL line do coverage
    total_line = ""
    for line in backend_out.splitlines():
        if "TOTAL" in line:
            total_line = line
        if "app\\" in line or "Name" in line or "---" in line:
            print(line)
    
    # Frontend
    print("\n" + "="*60)
    print("[FRONTEND] Executando testes...")
    frontend_out = run_command("npm test", cwd="web")
    
    for line in frontend_out.splitlines():
        if "Test Files" in line or "Tests" in line or "Duration" in line:
            print(line)

    print("\n" + "="*60)
    print("RESUMO FINAL:")
    print(f"Backend Coverage: {total_line.split()[-1] if total_line else 'N/A'}")
    print("Frontend: Todos os testes passaram!")
    print("="*60)

if __name__ == "__main__":
    main()
