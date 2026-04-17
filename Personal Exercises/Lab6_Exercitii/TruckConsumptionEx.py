import random
import pprint
def generate_data():
    fleet = []
    for t_id in range(100, 150):
        # Planned vs Actual
        truck = {
            "id": f"TRUCK-{t_id}",
            "plan": {"dist_km": 2500, "eta_hrs": 120, "consumption_rate": 16},
            "logs": [] # Hourly data
        }
        fuel = 400
        for h in range(168):
            dist_moved = random.uniform(15, 25)
            # Simulate Fuel Theft (Anomaly)
            fuel_loss = (dist_moved / 100) * truck["plan"]["consumption_rate"]
            if t_id == 105 and h == 20: fuel -= 50 # Theft event
            fuel -= fuel_loss
            
            truck["logs"].append({
                "hour": h,
                "gps_deviation": random.uniform(0, 15) if t_id != 110 else random.uniform(0, 60),
                "fuel_level": fuel,
                "dist_covered": dist_moved,
                "road_block": random.choice([True, False]) if random.random() > 0.95 else False
            })
        fleet.append(truck)
    return fleet

pprint.pprint(generate_data())

"""
Fleet Commander 2026 - Analyzer संरcture

Goal:
- Process fleet_data (list of trucks with logs)
- Generate:
    1. REPORT (efficiency metrics)
    2. ANOMALIES (suspicious behavior)

Constraints:
- Vanilla Python only
"""

# =========================
# CONFIGURATION
# =========================

FUEL_DROP_LIMIT = 10              # liters
GPS_DEV_LIMIT = 40               # km
MIN_CONSECUTIVE_HOURS = 3
MIN_MOVEMENT_THRESHOLD = 1       # km (defines "near zero")


# =========================
# MAIN ORCHESTRATOR
# =========================

def analyze_fleet(fleet_data):
    """
    Entry point for analysis.

    Responsibilities:
    - Call reporting engine
    - Call anomaly detection engine
    - Merge results into final structure

    Returns:
        dict: {
            "REPORT": {...},
            "ANOMALIES": {...}
        }
    """

    report = build_report(fleet_data)
    anomalies = detect_anomalies(fleet_data)

    return {
        "REPORT": report,
        "ANOMALIES": anomalies
    }


# =========================
# REPORTING ENGINE
# =========================

def build_report(fleet_data):
    """
    Builds per-truck metrics + fleet average.

    Steps:
    - Loop through each truck
    - Compute metrics using helper
    - Store results
    - Compute fleet average efficiency

    Returns:
        dict
    """

    report = {}
    efficiencies = []

    for truck in fleet_data:
        # Extract truck ID
        truck_id = truck["id"]

        # Process metrics
        metrics = process_truck_metrics(truck)

        # Store per-truck data
        report[truck_id] = metrics

        # Collect efficiency for fleet average
        efficiencies.append(metrics["efficiency"])

    # Compute fleet average efficiency
    # (guard against division by zero if needed)
    report["FLEET_AVG_EFFICIENCY"] = None  # TODO

    return report


def process_truck_metrics(truck):
    """
    Compute:
    - Total distance
    - Total fuel consumed
    - Efficiency score

    Key ideas:
    - Distance = sum of all dist_covered
    - Fuel consumed = initial fuel - final fuel
    - Planned fuel = based on plan.dist_km and consumption_rate

    Returns:
        dict: {
            "total_dist": float,
            "efficiency": float
        }
    """

    logs = truck["logs"]
    plan = truck["plan"]

    # --- TOTAL DISTANCE ---
    total_dist = None  # TODO: sum all dist_covered

    # --- FUEL CONSUMPTION ---
    # Hint:
    # initial fuel = logs[0]["fuel_level"] (or inferred)
    # final fuel = logs[-1]["fuel_level"]
    fuel_consumed = None  # TODO

    # --- PLANNED CONSUMPTION ---
    planned_consumption = None  # TODO

    # --- EFFICIENCY ---
    efficiency = None  # TODO

    return {
        "total_dist": total_dist,
        "efficiency": efficiency
    }


# =========================
# ANOMALY DETECTION ENGINE
# =========================

def detect_anomalies(fleet_data):
    """
    Detect anomalies per truck.

    Steps:
    - Loop through trucks
    - Run:
        - fuel theft detection
        - route deviation detection
    - Combine results

    Returns:
        dict: {
            "TRUCK-XXX": [list of reasons]
        }
    """

    suspects = {}

    for truck in fleet_data:
        truck_id = truck["id"]
        logs = truck["logs"]

        # Run detection functions
        fuel_flags = detect_fuel_theft(logs)
        route_flags = detect_route_deviation(logs)

        # Combine results
        all_flags = fuel_flags + route_flags

        # Store only if suspicious
        if all_flags:
            suspects[truck_id] = all_flags

    return suspects


# =========================
# FUEL THEFT DETECTION
# =========================

def detect_fuel_theft(logs):
    """
    Detect abnormal fuel drops.

    Logic:
    - Iterate from second log
    - Compare fuel difference with previous hour
    - Check:
        fuel_drop > FUEL_DROP_LIMIT
        AND
        distance is near zero

    Returns:
        list of strings describing events
    """

    flags = []

    # Loop through logs starting from index 1
    for i in range(1, len(logs)):
        prev_log = logs[i - 1]
        curr_log = logs[i]

        # Compute fuel drop
        fuel_drop = None  # TODO

        # Extract distance
        distance = curr_log["dist_covered"]

        # Condition check
        # if fuel_drop > limit AND distance < threshold:
        #     append descriptive message with hour

    return flags


# =========================
# ROUTE DEVIATION DETECTION
# =========================

def detect_route_deviation(logs):
    """
    Detect sustained GPS deviation.

    Logic:
    - Track consecutive hours where gps_deviation > limit
    - If exceeds MIN_CONSECUTIVE_HOURS → flag

    Optimization:
    - Break early once detected

    Returns:
        list of strings
    """

    flags = []
    consecutive = 0

    for log in logs:
        deviation = log["gps_deviation"]

        # If above threshold → increment counter
        # Else → reset counter

        # If counter exceeds MIN_CONSECUTIVE_HOURS:
        #     append message
        #     break (optimization)

    return flags


# =========================
# OPTIONAL: ENTRY POINT
# =========================

if __name__ == "__main__":
    """
    Suggested usage:
    - Import or generate fleet_data
    - Call analyze_fleet
    - Pretty print result
    """

    # Example:
    # from data_generator import generate_data
    # fleet_data = generate_data()

    # result = analyze_fleet(fleet_data)

    # print(result)

    pass