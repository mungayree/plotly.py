import _plotly_utils.basevalidators


class IntensitysrcValidator(_plotly_utils.basevalidators.SrcValidator):

    def __init__(
        self, plotly_name='intensitysrc', parent_name='mesh3d', **kwargs
    ):
        super(IntensitysrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='none',
            role='info',
            **kwargs
        )
