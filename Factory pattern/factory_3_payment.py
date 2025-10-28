from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardGateway(PaymentGateway):
    def pay(self, amount):
        print(f"Оплата {amount:.2f} USD через КРЕДИТНУЮ КАРТУ (Visa/MC).")

class PayPalGateway(PaymentGateway):
    def pay(self, amount):
        print(f"Перенаправление на PayPal для оплаты {amount:.2f} USD.")

class CryptoGateway(PaymentGateway):
    def pay(self, amount):
        print(f"Генерация крипто-адреса для оплаты {amount:.2f} USD.")

class PaymentFactory:
    def get_payment_gateway(self, method_type) -> PaymentGateway:
        payments = {
            'credit_card': CreditCardGateway(), 
            'paypal': PayPalGateway(),
            'crypto': CryptoGateway()
        }

        if method_type not in payments:
            raise ValueError(f"Unsupported type of payment method: {method_type}")
        return payments[method_type]
    
print("\n--- Пример с Простой Фабрикой (Платежи) ---")
class Store:
    def __init__(self):
        self.payment_factory = PaymentFactory()

    def checkout(self, amount, payment_method):
        print(f"\nНачало оформления заказа на {amount} USD...")
        try:
            gateaway = self.payment_factory.get_payment_gateway(payment_method)
            gateaway.pay(amount)
            print("Заказ успешно оплачен!")
        except ValueError as e:
            print(f"Ошибка оплаты: {e}")

mystore = Store()

mystore.checkout(199, 'credit_card')

mystore.checkout(999, 'paypal')

mystore.checkout(499, 'crypto')