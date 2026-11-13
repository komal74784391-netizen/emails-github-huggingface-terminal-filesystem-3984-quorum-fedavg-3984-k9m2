"""Bandwidth-aware federated averaging."""


def schedule(clients, bandwidth):
    return sorted(clients, key=lambda c: bandwidth[c], reverse=True)
