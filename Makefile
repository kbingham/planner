
FLASK = FLASK_APP=planner.py python3 -m flask

run:
	$(DEBUG) $(FLASK) run

open:
	xdg-open http://127.0.0.1:5000/


debug: DEBUG=FLASK_DEBUG=1
debug: run
