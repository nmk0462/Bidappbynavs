from django.contrib import admin
from .models import User
from .models import Listings
from .models import Bids
from .models import Comments
from .models import Watchlist
from .models import Winners1
from django.contrib.auth.admin import UserAdmin
# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Listings)
admin.site.register(Bids)
admin.site.register(Comments)
admin.site.register(Watchlist)
admin.site.register(Winners1)