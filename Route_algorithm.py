import math

# ----------------------------
# Configuration parameters
# ----------------------------
MAX_PICKUP_DIST = 20.0
MAX_EXTRA_DIST = 25.0
ACCEPT_THRESHOLD = 6.0  # score from 1–10


# ----------------------------
# Distance function
# ----------------------------
def distance(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])


# ----------------------------
# Event model
# ----------------------------
class Event:
    def __init__(self, kind, pid, loc):
        self.kind = kind  # "PU" or "DO"
        self.pid = pid
        self.loc = loc

def route_length_events(route, start):
    length = 0.0
    current = start
    for ev in route:
        length += distance(current, ev.loc)
        current = ev.loc
    return length

def best_insertion(route, start, pickup_loc, dropoff_loc, new_pid):
    best_extra = float("inf")
    best_route = None

    base_len = route_length_events(route, start)

    n = len(route)

    for i in range(n + 1):
        pu_event = Event("PU", new_pid, pickup_loc)

        for j in range(i + 1, n + 2):
            do_event = Event("DO", new_pid, dropoff_loc)

            candidate = route[:i] + [pu_event] + route[i:j-1] + [do_event] + route[j-1:]

            new_len = route_length_events(candidate, start)
            extra = new_len - base_len

            if extra < best_extra:
                best_extra = extra
                best_route = candidate

    return best_extra, best_route

# ----------------------------
# Bus model
# ----------------------------
class Bus:
    def __init__(self, start=(0, 0)):
        self.position = start
        self.route = []
        self.next_pid = 1

    def __str__(self):
        if not self.route:
            return f"Bus at {self.position}, route empty"
        s = f"Bus at {self.position}, route:\n"
        for i, ev in enumerate(self.route):
            s += f"  {i+1}. {ev.kind} P{ev.pid} at {ev.loc}\n"
        return s

    def evaluate_request(self, pickup, dropoff):
        # Quick rejection: pickup too far
        if distance(self.position, pickup) > MAX_PICKUP_DIST:
            return 0.0, None

        extra, new_route = best_insertion(
            self.route,
            self.position,
            pickup,
            dropoff,
            self.next_pid
        )

        if extra > MAX_EXTRA_DIST:
            return 0.0, None

        score = 10 * (1 - extra / MAX_EXTRA_DIST)
        score = max(1.0, min(10.0, score))

        return score, new_route

    def apply_route(self, new_route):
        self.route = new_route
        self.next_pid += 1


# ----------------------------
# Main loop
# ----------------------------
def main():
    bus = Bus()

    print("On-Demand Bus Route Simulator")
    print("Enter requests as: x_pickup y_pickup x_dest y_dest")
    print("Type 'exit' to quit\n")

    while True:
        print(bus)
        user_input = input("Request> ").strip()

        if user_input.lower() == "exit":
            break

        try:
            x1, y1, x2, y2 = map(float, user_input.split())
            pickup = (x1, y1)
            dropoff = (x2, y2)
        except ValueError:
            print("Invalid input format\n")
            continue

        score, new_route = bus.evaluate_request(pickup, dropoff)

        print(f"Score: {score:.2f}")

        if score >= ACCEPT_THRESHOLD:
            print("Request ACCEPTED ✅")
            bus.apply_route(new_route)
        else:
            print("Request REJECTED ❌")

        print()


if __name__ == "__main__":
    main()
