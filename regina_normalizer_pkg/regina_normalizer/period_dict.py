#TODO: this should be automatically generated, changes in dict have to be represented here as well
# How about ignore case when matching?
period_ptrn = r"\b(mán(ud)?|þri(ðjud)?|miðvikud|fim(mtud)?|fös(tud)?|lau(gard)|sun(nud)|[Jj]an|[Ff]eb|[Mm]ar|[Aa]pr|[Jj]ú[nl]|[Áá]gú?|[Ss]ept?|[Oo]kt|[Nn]óv|[Dd]es)\.?|\b(I(II?|V|X)|(V|X|XV)I{1,3}|XI?[VX])\b"
                         
def make_period_dict():
    period_dict = {"(\W|^)mán(ud)?\.?(\W|$)": "\g<1>mánudag\g<3>",
                    "(\W|^)þri(ðjud)?\.?(\W|$)": "\g<1>þriðjudag\g<3>",
                    "(\W|^)miðvikud\.?(\W|$)": "\g<1>miðvikudag\g<2>",
                    "(\W|^)fim(mtud)?\.?(\W|$)": "\g<1>fimmtudag\g<3>",
                    "(\W|^)fös(tud)?\.?(\W|$)": "\g<1>föstudag\g<3>",
                    "(\W|^)lau(gard)?\.?(\W|$)": "\g<1>laugardag\g<3>",
                    "(\W|^)sun(nud)?\.?(\W|$)": "\g<1>sunnudag\g<3>",

                    "(\W|^)[Jj]an\.?(\W|$)": "\g<1>janúar\g<2>",
                    "(\W|^)[Ff]eb\.?(\W|$)": "\g<1>febrúar\g<2>",
                    "(\W|^)[Mm]ar\.?(\W|$)": "\g<1>mars\g<2>",
                    "(\W|^)[Aa]pr\.?(\W|$)": "\g<1>apríl\g<2>",
                    "(\W|^)[Jj]ún\.?(\W|$)": "\g<1>júní\g<2>",
                    "(\W|^)[Jj]úl\.?(\W|$)": "\g<1>júlí\g<2>",
                    "(\W|^)[Áá]gú?\.?(\W|$)": "\g<1>ágúst\g<2>",
                    "(\W|^)[Ss]ept?\.?(\W|$)": "\g<1>september\g<2>",
                    "(\W|^)[Oo]kt\.?(\W|$)": "\g<1>október\g<2>",
                    "(\W|^)[Nn]óv\.?(\W|$)": "\g<1>nóvember\g<2>",
                    "(\W|^)[Dd]es\.?(\W|$)": "\g<1>desember\g<2>",

                    "(\W|^)II\.?(\W|$)": "\g<1>annar\g<2>",
                    "(\W|^)III\.?(\W|$)": "\g<1>þriðji\g<2>",
                    "(\W|^)IV\.?(\W|$)": "\g<1>fjórði\g<2>",
                    "(\W|^)VI\.?(\W|$)": "\g<1>sjötti\g<2>",
                    "(\W|^)VII\.?(\W|$)": "\g<1>sjöundi\g<2>",
                    "(\W|^)VIII\.?(\W|$)": "\g<1>áttundi\g<2>",
                    "(\W|^)IX\.?(\W|$)": "\g<1>níundi\g<2>",
                    "(\W|^)XI\.?(\W|$)": "\g<1>ellefti\g<2>",
                    "(\W|^)XII\.?(\W|$)": "\g<1>tólfti\g<2>",
                    "(\W|^)XIII\.?(\W|$)": "\g<1>þrettándi\g<2>",
                    "(\W|^)XIV\.?(\W|$)": "\g<1>fjórtándi\g<2>",
                    "(\W|^)XV\.?(\W|$)": "\g<1>fimmtándi\g<2>",
                    "(\W|^)XVI\.?(\W|$)": "\g<1>sextándi\g<2>",
                    "(\W|^)XVII\.?(\W|$)": "\g<1>sautjándi\g<2>",
                    "(\W|^)XVIII\.?(\W|$)": "\g<1>átjándi\g<2>",
                    "(\W|^)XIX\.?(\W|$)": "\g<1>nítjándi\g<2>"}
    
    return period_dict