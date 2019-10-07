"""Auto-generated file, do not edit by hand. KR metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_KR = PhoneMetadata(id='KR', country_code=82, international_prefix='00(?:[125689]|3(?:[46]5|91)|7(?:00|27|3|55|6[126]))',
    general_desc=PhoneNumberDesc(national_number_pattern='00[1-9]\\d{8,11}|(?:[12]|5\\d{3})\\d{7}|[13-6]\\d{9}|(?:[1-6]\\d|80)\\d{7}|[3-6]\\d{4,5}|(?:00|7)0\\d{8}', possible_length=(5, 6, 8, 9, 10, 11, 12, 13, 14), possible_length_local_only=(3, 4, 7)),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:2|3[1-3]|[46][1-4]|5[1-5])[1-9]\\d{6,7}|(?:3[1-3]|[46][1-4]|5[1-5])1\\d{2,3}', example_number='22123456', possible_length=(5, 6, 8, 9, 10), possible_length_local_only=(3, 4, 7)),
    mobile=PhoneNumberDesc(national_number_pattern='10[01]\\d{6}|1(?:0[2-9]|[126-9]\\d)\\d{6,7}', example_number='1020000000', possible_length=(9, 10)),
    toll_free=PhoneNumberDesc(national_number_pattern='00(?:308\\d{6,7}|798\\d{7,9})|(?:00368|80)\\d{7}', example_number='801234567', possible_length=(9, 11, 12, 13, 14)),
    premium_rate=PhoneNumberDesc(national_number_pattern='60[2-9]\\d{6}', example_number='602345678', possible_length=(9,)),
    personal_number=PhoneNumberDesc(national_number_pattern='50\\d{8,9}', example_number='5012345678', possible_length=(10, 11)),
    voip=PhoneNumberDesc(national_number_pattern='70\\d{8}', example_number='7012345678', possible_length=(10,)),
    pager=PhoneNumberDesc(national_number_pattern='15\\d{7,8}', example_number='1523456789', possible_length=(9, 10)),
    uan=PhoneNumberDesc(national_number_pattern='1(?:5(?:22|44|66|77|88|99)|6(?:[07]0|44|6[16]|88)|8(?:00|33|55|77|99))\\d{4}', example_number='15441234', possible_length=(8,)),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='00(?:3(?:08\\d{6,7}|68\\d{7})|798\\d{7,9})', possible_length=(11, 12, 13, 14)),
    national_prefix='0',
    national_prefix_for_parsing='0(8(?:[1-46-8]|5\\d\\d))?',
    number_format=[NumberFormat(pattern='(\\d{5})', format='\\1', leading_digits_pattern=['1[016-9]1', '1[016-9]11', '1[016-9]114'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d{2})(\\d{3,4})', format='\\1-\\2', leading_digits_pattern=['(?:3[1-3]|[46][1-4]|5[1-5])1'], national_prefix_formatting_rule='0\\1', domestic_carrier_code_formatting_rule='0$CC-\\1'),
        NumberFormat(pattern='(\\d{4})(\\d{4})', format='\\1-\\2', leading_digits_pattern=['1']),
        NumberFormat(pattern='(\\d)(\\d{3,4})(\\d{4})', format='\\1-\\2-\\3', leading_digits_pattern=['2'], national_prefix_formatting_rule='0\\1', domestic_carrier_code_formatting_rule='0$CC-\\1'),
        NumberFormat(pattern='(\\d{2})(\\d{3})(\\d{4})', format='\\1-\\2-\\3', leading_digits_pattern=['60|8'], national_prefix_formatting_rule='0\\1', domestic_carrier_code_formatting_rule='0$CC-\\1'),
        NumberFormat(pattern='(\\d{2})(\\d{3,4})(\\d{4})', format='\\1-\\2-\\3', leading_digits_pattern=['[1346]|5[1-5]'], national_prefix_formatting_rule='0\\1', domestic_carrier_code_formatting_rule='0$CC-\\1'),
        NumberFormat(pattern='(\\d{2})(\\d{4})(\\d{4})', format='\\1-\\2-\\3', leading_digits_pattern=['[57]'], national_prefix_formatting_rule='0\\1', domestic_carrier_code_formatting_rule='0$CC-\\1'),
        NumberFormat(pattern='(\\d{5})(\\d{3})(\\d{3})', format='\\1 \\2 \\3', leading_digits_pattern=['003', '0030']),
        NumberFormat(pattern='(\\d{2})(\\d{5})(\\d{4})', format='\\1-\\2-\\3', leading_digits_pattern=['5'], national_prefix_formatting_rule='0\\1', domestic_carrier_code_formatting_rule='0$CC-\\1'),
        NumberFormat(pattern='(\\d{5})(\\d{3,4})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['0']),
        NumberFormat(pattern='(\\d{5})(\\d{2})(\\d{3})(\\d{4})', format='\\1 \\2 \\3 \\4', leading_digits_pattern=['0'])],
    intl_number_format=[NumberFormat(pattern='(\\d{2})(\\d{3,4})', format='\\1-\\2', leading_digits_pattern=['(?:3[1-3]|[46][1-4]|5[1-5])1']),
        NumberFormat(pattern='(\\d{4})(\\d{4})', format='\\1-\\2', leading_digits_pattern=['1']),
        NumberFormat(pattern='(\\d)(\\d{3,4})(\\d{4})', format='\\1-\\2-\\3', leading_digits_pattern=['2']),
        NumberFormat(pattern='(\\d{2})(\\d{3})(\\d{4})', format='\\1-\\2-\\3', leading_digits_pattern=['60|8']),
        NumberFormat(pattern='(\\d{2})(\\d{3,4})(\\d{4})', format='\\1-\\2-\\3', leading_digits_pattern=['[1346]|5[1-5]']),
        NumberFormat(pattern='(\\d{2})(\\d{4})(\\d{4})', format='\\1-\\2-\\3', leading_digits_pattern=['[57]']),
        NumberFormat(pattern='(\\d{2})(\\d{5})(\\d{4})', format='\\1-\\2-\\3', leading_digits_pattern=['5'])],
    mobile_number_portable_region=True)
