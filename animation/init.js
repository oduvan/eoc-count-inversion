requirejs(['ext_editor_io', 'jquery_190', 'raphael_210'],
    function (extIO, $, TableComponent) {
        var io = new extIO({
            functions: {
                js: 'countInversion',
                python: 'count_inversion'
            }
        });
        io.start();
    }
);