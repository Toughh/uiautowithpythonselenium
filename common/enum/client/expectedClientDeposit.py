import enum


class ExpectedClientDeposit(enum.Enum):
    client_deposit1 = '$1,000 - $9,999'
    client_deposit2 = '$10,000 - $49,999'
    client_deposit3 = '$50,000 - $100,000'
    client_deposit4 = '$100,000+'
