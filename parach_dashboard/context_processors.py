
from parach_dashboard.models import BranchLocation
def locationsView(request):
    locations = BranchLocation.objects.all()

    return{
        'locations':locations
    }
