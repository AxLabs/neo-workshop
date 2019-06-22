from boa.interop.Neo.Runtime import CheckWitness
from boa.interop.Neo.Storage import Get, Put, Delete, GetContext

ctx = GetContext()


def Main(operation, name, addr):
    if operation == 'register':
        return register(ctx, name, addr)

    elif operation == 'query':
        return Get(ctx, name)

    elif operation == 'delete':
        return delete(ctx, name)

    return False


def register(ctx, name, addr):
    if not is_valid_addr(addr):
        return False
    if not CheckWitness(addr):
        return False
    addr_value = Get(ctx, name)
    if addr_value is not None:
        return False
    Put(ctx, name, addr)
    return True


def query(ctx, name):
    return Get(ctx, name)


def delete(ctx, name):
    owner = Get(ctx, name)
    if owner is None:
        return False
    if not CheckWitness(owner):
        return False
    Delete(ctx, name)
    return True


def is_valid_addr(addr):
    if len(addr) == 20:
        return True
    return False
