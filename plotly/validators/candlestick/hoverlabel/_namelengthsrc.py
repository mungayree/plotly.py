import _plotly_utils.basevalidators


class NamelengthsrcValidator(_plotly_utils.basevalidators.SrcValidator):

    def __init__(
        self,
        plotly_name='namelengthsrc',
        parent_name='candlestick.hoverlabel',
        **kwargs
    ):
        super(NamelengthsrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='none',
            role='info',
            **kwargs
        )
