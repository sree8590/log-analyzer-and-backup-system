from validator import validate_record
from utils.decorator import log_execution


@log_execution
def process_records(records):

    valid_records = list(filter(validate_record, records))

    processed_records = list(
        map(
            lambda record: (
                record.split()[0].upper(),
                record.split()[1],
                record.split()[2]
            ),
            valid_records
        )
    )

    return processed_records


def get_invalid_records(records):

    invalid_records = list(
        filter(lambda record: not validate_record(record), records)
    )

    return invalid_records