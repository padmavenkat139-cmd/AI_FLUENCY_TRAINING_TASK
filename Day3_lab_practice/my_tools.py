# One simple external tool for the AI agent

BUS_SCHEDULE = {
    "B1": {
        "departure": "7:30 AM",
        "first_stop": "Main Gate",
        "final_stop": "Central Railway Station"
    },
    "B2": {
        "departure": "7:45 AM",
        "first_stop": "Main Gate",
        "final_stop": "Gandhi Nagar"
    },
    "B3": {
        "departure": "8:00 AM",
        "first_stop": "College Campus",
        "final_stop": "Town Bus Stand"
    },
    "B4": {
        "departure": "8:15 AM",
        "first_stop": "College Campus",
        "final_stop": "Market Road"
    }
}


def lookup_bus_schedule(route):
    """Look up the private college bus schedule."""

    route = route.upper()

    if route in BUS_SCHEDULE:
        bus = BUS_SCHEDULE[route]

        return (
            f"Route {route}: "
            f"Departure: {bus['departure']}; "
            f"First stop: {bus['first_stop']}; "
            f"Final stop: {bus['final_stop']}."
        )

    return f"No schedule found for route {route}."