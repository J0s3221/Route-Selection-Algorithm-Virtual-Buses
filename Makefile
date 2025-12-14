PYTHON = python3
SCRIPT = Route_algorithm.py
SCENARIOS = scenarios

.PHONY: help interactive uc1 uc2 uc3 uc4 uc5 all

help:
	@echo "Available targets:"
	@echo "  make interactive   Run interactive mode"
	@echo "  make uc1           Use Case 1: Basic pickup"
	@echo "  make uc2           Use Case 2: Pickup on the way"
	@echo "  make uc3           Use Case 3: Pickup before first stop"
	@echo "  make uc4           Use Case 4: Request rejection"
	@echo "  make uc5           Use Case 5: Multiple sequential requests"
	@echo "  make all           Run all use cases"

interactive:
	$(PYTHON) $(SCRIPT)

uc1:
	@echo "=== Use Case 1: Basic On-Demand Pickup ==="
	$(PYTHON) $(SCRIPT) < $(SCENARIOS)/uc1_basic.txt

uc2:
	@echo "=== Use Case 2: Pickup On The Way ==="
	$(PYTHON) $(SCRIPT) < $(SCENARIOS)/uc2_on_the_way.txt

uc3:
	@echo "=== Use Case 3: Pickup Before First Stop ==="
	$(PYTHON) $(SCRIPT) < $(SCENARIOS)/uc3_before_first_stop.txt

uc4:
	@echo "=== Use Case 4: Request Rejection ==="
	$(PYTHON) $(SCRIPT) < $(SCENARIOS)/uc4_rejection.txt

uc5:
	@echo "=== Use Case 5: Multiple Sequential Requests ==="
	$(PYTHON) $(SCRIPT) < $(SCENARIOS)/uc5_multiple_requests.txt

all: uc1 uc2 uc3 uc4 uc5
