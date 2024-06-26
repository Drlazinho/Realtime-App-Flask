import qrcode
import uuid

class Pix:
    def __init__(self):
        pass

    def create_payment(self, base_dir=""):
        # criar o pagamento na instituicao financeira
        bank_payment_id = str(uuid.uuid4())

        # codigo copia e cola
        hash_payment = f'hash_payement_{bank_payment_id}'
        
        # qr code -> gerar img
        img = qrcode.make(hash_payment)
        # salvar a img
        img.save(f"{base_dir}static/img/qr_code_payment_{bank_payment_id}.png")
        
        return {
            "bank_payment_id": bank_payment_id,
            "qr_code_path": f"qr_code_payment_{bank_payment_id}",
        }