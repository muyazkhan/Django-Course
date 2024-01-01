from django.urls import path
from .import views
urlpatterns = [ 
    path('deposit/', views.deposit_view.as_view(),name='deposit_money'),
    path('withdraw/', views.WithdrawMoneyView.as_view(),name='withdraw_money'),
    path('loanList/', views.LoanListView.as_view(),name='loan_list'),
    path('loanRequest/', views.LoanRequestView.as_view(),name='loan_request'),
    path('MoneyTransfer/', views.MoneyTransferView.as_view(),name='Money_Transfer'),
    path('report/', views.TransactionReportView.as_view(),name='transaction_report'),
    path('payLoan/<int:loan_id>/', views.PayLoanView.as_view(),name='pay'),
]   