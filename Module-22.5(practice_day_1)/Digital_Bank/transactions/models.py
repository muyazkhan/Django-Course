from django.db import models
from accounts.models import UserAccount
# Create your models here.
DEPOSIT =1
WITHDRAW=2
LOAN = 3
LOAN_PAID = 4
MONEY_TRANSFER = 5

TRANSACTION_TYPE = (
    (1, 'deposit'),
    (2, 'withdraw'),
    (3, 'Loan'),
    (4, 'Loan paid'),
    (5, 'Money transfer'),
)


class Transaction(models.Model):
    account = models.ForeignKey( UserAccount, related_name='transactions', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    balance_after_transaction = models.DecimalField( max_digits=12, decimal_places=2)
    transaction_type = models.IntegerField(choices=TRANSACTION_TYPE, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    loan_approve = models.BooleanField(default=False)

    class Meta:
        ordering = ['timestamp']

class MoneyTransfer(models.Model):
    account = models.ForeignKey(UserAccount, related_name='transfers', on_delete=models.CASCADE)
    receiver = models.DecimalField(max_digits=12, decimal_places=0)
    balance_after_transaction = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True)
    transaction_type = models.IntegerField(choices=TRANSACTION_TYPE, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True)

    class Meta:
        ordering = ['timestamp']

    def __str__(self) -> str:
        return str(self.receiver)