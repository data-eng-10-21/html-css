from src.models.position import Position

def test_init_position():
    position = Position(*['2bcc7676b2ad9c78', 'Data Engineer', [50000, 150000], 
     'New York', 'NY', 'Qloo'])
    assert list(position.__dict__.values()) == ['2bcc7676b2ad9c78', 'Data Engineer', [50000, 150000], 
     'New York', 'NY', 'Qloo']