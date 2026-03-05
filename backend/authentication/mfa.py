# Epic Title: Implement Secure Login Mechanism

import random
import string
import secrets

class MFA:
    @staticmethod
    def generate_otp() -> str:
        return ''.join(secrets.choice(string.digits) for _ in range(6))

    @staticmethod
    def verify_otp(input_otp: str, valid_otp: str) -> bool:
        return secrets.compare_digest(input_otp, valid_otp)