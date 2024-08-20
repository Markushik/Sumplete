from dishka.integrations.base import wrap_injection


def inject_getter(func):
    return wrap_injection(
        func=func,
        container_getter=lambda _, p: p["dishka_container"],
        is_async=True,
    )


def inject_handler(func):
    return wrap_injection(
        func=func,
        container_getter=lambda p, _: p[2].middleware_data["dishka_container"],
        is_async=True,
    )
