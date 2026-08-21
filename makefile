.PHONY: all help envs bundle-install schedule schedule-fall schedule-spring calendar-ics serve serve-fall serve-spring serve-4001 stop-serve build-site clean-schedule-data

all: schedule-fall

help:
	@echo "Simple workflow"
	@echo "  1) make envs"
	@echo "  2) conda activate ./envs"
	@echo "  3) make serve"
	@echo ""
	@echo "Commands"
	@echo "  make envs"
	@echo "  make bundle-install"
	@echo "  make schedule-fall"
	@echo "  make schedule-spring"
	@echo "  make calendar-ics"
	@echo "  make serve"
	@echo "  make serve-spring"
	@echo "  make serve-4001"
	@echo "  make stop-serve"
	@echo "  make build-site"

envs:
	@if [ -d "./envs" ]; then \
		conda env update --prefix ./envs --file environment.yml --prune; \
	else \
		conda env create --prefix ./envs --file environment.yml; \
	fi

bundle-install:
	./envs/bin/bundle install

schedule: schedule-fall

schedule-fall:
	./envs/bin/python scripts/update_schedule.py \
		--calendar config/fall_calendar.yml \
		--schedule-dir Schedule \
		--schedule-data _data/schedule.yml \
		--schedule-warnings _data/schedule_warnings.yml
	./envs/bin/python scripts/generate_course_calendar.py \
		--schedule-data _data/schedule.yml \
		--config _config.yml \
		--output course_calendar.ics

schedule-spring:
	./envs/bin/python scripts/update_schedule.py \
		--calendar config/spring_calendar.yml \
		--schedule-dir Schedule \
		--schedule-data _data/schedule.yml \
		--schedule-warnings _data/schedule_warnings.yml
	./envs/bin/python scripts/generate_course_calendar.py \
		--schedule-data _data/schedule.yml \
		--config _config.yml \
		--output course_calendar.ics

calendar-ics:
	./envs/bin/python scripts/generate_course_calendar.py \
		--schedule-data _data/schedule.yml \
		--config _config.yml \
		--output course_calendar.ics

serve: serve-fall

serve-fall: schedule-fall bundle-install
	./envs/bin/bundle exec jekyll serve --source . --trace

serve-spring: schedule-spring bundle-install
	./envs/bin/bundle exec jekyll serve --source . --trace

serve-4001: schedule-fall bundle-install
	./envs/bin/bundle exec jekyll serve --source . --trace --port 4001

stop-serve:
	@lsof -tiTCP:4000 -sTCP:LISTEN | xargs kill -9 2>/dev/null || true
	@lsof -tiTCP:4001 -sTCP:LISTEN | xargs kill -9 2>/dev/null || true

build-site: schedule-fall bundle-install
	./envs/bin/bundle exec jekyll build --source . --trace

clean-schedule-data:
	rm -f _data/schedule.yml _data/schedule_warnings.yml course_calendar.ics

serve-local:
	PAGES_REPO_NWO=local/test-repo make serve
