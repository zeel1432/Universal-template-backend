# Universal FastAPI Backend Template

This is a reusable FastAPI backend template with a stable core and pluggable business modules.

The `app/` folder contains the core architecture; everything above `modules/` is designed to stay the same across projects.

You can add new business domains under `app/modules/` (for example `products`, `orders`, `bookings`) and wire their routers into `app/main.py`.
