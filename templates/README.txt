# Frontend-only Starter (HTML/CSS)

This is a static site matching the Warwick SU Clubs MVP pages. It is backend-ready: each page has placeholders and IDs for easy wiring.

## Pages
- index.html — Home (static demo of clubs + upcoming bookings)
- rooms.html — Rooms table (id="room-table")
- schedule.html — Daily schedule (static sample)
- book.html — Book form (static; to be restricted to exec later)
- bookings.html — My Club Bookings table (id="my-bookings")
- login.html, register.html — Demo forms
- index_loggedin_exec.html / index_loggedin_member.html — role mockups for screenshots

## Handoff to backend
- Move this folder under Flask's /templates (HTML) and /static (assets) OR serve as pure static first.
- Replace static links with Flask url_for helpers on integration:
  <link rel="stylesheet" href="assets/css/style.css">
  becomes
  <link rel="stylesheet" href="{{ url_for('static', filename='assets/css/style.css') }}">
- Replace static tables with template loops (Jinja) or fetch via /api/... .

## Preview
Just open index.html in a browser. No Python required.
