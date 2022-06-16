from django.contrib import admin

from transactions.models import Transaction, Pot , GreenMember , RedMember , CurrentPrice , CandleColor

admin.site.register(Transaction)
admin.site.register(Pot)
admin.site.register(GreenMember)
admin.site.register(RedMember)
admin.site.register(CurrentPrice)
admin.site.register(CandleColor)


