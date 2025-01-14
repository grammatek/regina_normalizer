pre_help_dicts = {r"(\W|^)(?i)2ja(\W|$)": '\g<1>tveggja\g<2>',
			    r"(\W|^)(?i)3ja(\W|$)": '\g<1>þriggja\g<2>',
			    r"(\W|^)(?i)4ð(a|i)(\W|$)": '\g<1>fjórð\g<2>\g<3>',
			    r"(\W|^)(?i)5t(a|i)(\W|$)": '\g<1>fimmt\g<2>\g<3>',
			    r"(\W|^)(?i)6t(a|i)(\W|$)": '\g<1>sjött\g<2>\g<3>',
			    r"(\W|^)(?i)7d(a|i)(\W|$)": '\g<1>sjöund\g<2>\g<3>',
			    r"(\W|^)(?i)8d(a|i)(\W|$)": '\g<1>áttund\g<2>\g<3>',
			    r"(\W|^)(?i)9d(a|i)(\W|$)": '\g<1>níund\g<2>\g<3>',
			    
			    r"(?i)([a-záðéíóúýþæö]+)(\d+)": '\g<1> \g<2>',
			    r"(?i)(\d+)([a-záðéíóúýþæö]+)": '\g<1> \g<2>',
			    r"(\W|^)([A-ZÁÐÉÍÓÚÝÞÆÖ]+)(\-[A-ZÁÐÉÍÓÚÝÞÆÖa-záðéíóúýþæö]+)(\W|$)": "\g<1>\g<2> \g<3>\g<4>",
			    r"(\W|^)([A-ZÁÐÉÍÓÚÝÞÆÖa-záðéíóúýþæö]+\-)([A-ZÁÐÉÍÓÚÝÞÆÖ]+)(\W|$)": "\g<1>\g<2> \g<3>\g<4>",
			    r"(?i)([\da-záðéíóúýþæö]+)(°)": '\g<1> \g<2>',
			    r"(?i)([\da-záðéíóúýþæö]+)(\%)": '\g<1> \g<2>',
			    r"(\W|^)(0?[1-9]|[12]\d|3[01])\.(0?[1-9]|1[012])\.(\d{3,4})(\W|$)": " \g<1>\g<2>. \g<3>. \g<4>\g<5>",	
			    r"(\W|^)(0?[1-9]|[12]\d|3[01])\.(0?[1-9]|1[012])\.(\W|$)": " \g<1>\g<2>. \g<3>.\g<4>",
				  # reformat telephone numbers to ddd-dddd
			    "(\d{3})( )(\d{4})": " \g<1>-\g<3>"}