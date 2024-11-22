import secrets
import time
#python gerador_mfa.py para iniciar
#precisa ter o python instalado

def generate_otp():
    """Gera um código OTP (One-Time Password) de 8 dígitos."""
    otp = secrets.randbits(32) % 100000000  # Gera um número aleatório entre 0 e 99999999
    return str(otp).zfill(8)  # Garante que o número tenha 8 dígitos

def main():
    while True:
        otp = generate_otp()
        print(f"Código MFA: {otp}")
        time.sleep(15)  # Aguarda 15 segundos

if __name__ == "__main__":
    main()