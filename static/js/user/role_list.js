layui.use(['layer', 'form', 'table', 'jquery'], function () {
    var $ = layui.$ //重点处
        , layer = layui.layer
        , form = layui.form
        , table = layui.table
        , transfer = layui.transfer;

    // 创建角色
    var createUrl = $("input[name='url_role_create']").val();
    // 角色列表
    var roleUrl = $("input[name='url_role_list']").val();
    // 角色数据表格
    var dataUrl = $("input[name='url_role_data']").val();
    


    /**
     * 角色表格渲染
     */
    table.render({
        elem: '#role_table'
        , height: 420
        , url: dataUrl //数据接口
        , title: '用户表'
        , id: 'role'
        , page: true //开启分页
        // , toolbar: 'default' //开启工具栏，此处显示默认图标，可以自定义模板，详见文档
        , toolbar: '#toolbarDemo'//开启自定义工具行，指向自定义工具栏模板选择器 https://www.jb51.net/article/170339.htm
        // , defaultToolbar: ['filter', 'print', 'exports']
        , totalRow: true //开启合计行
        , cols: [[ //表头
            {type: 'checkbox', fixed: 'left'}
            , {field: 'id', title: 'ID', sort: true, fixed: 'left', align: 'center', totalRowText: '合计：'}
            , {field: 'name', title: '角色名称', align: 'center'}
            // , {field: 'password', title: '密码', align: 'center'}
            // , {field: 'phone', title: '手机号码', align: 'center'}
            // , {field: 'email', title: '邮箱', align: 'center'}
            , {fixed: 'right', title: '操作', align: 'center', toolbar: '#barDemo'}
        ]]
    });


    /**
     * 表格监听事件
     */
    table.on('toolbar(role_action)', function (obj) {
        var checkStatus = table.checkStatus(obj.config.id)
            , data = checkStatus.data; //获取选中的数据
        switch (obj.event) {
            case 'role_create':
                layer.msg('添加');
                layer.open({
                    title: '在线调试'
                    // , area: ['500px', '300px']
                    , area: '600px'
                    , content: $('#role_popup').html()
                    , yes: function (index, layero) {
                        console.log('回调函数')
                        // 获取角色名称
                        var role_name = $('#role').val();
                        //TODO 校验
                        $.get(createUrl, {role_name: role_name},
                            function (result) {
                                console.log(result)
                                // 表格重载
                                table.reload('role', {
                                    page: {
                                        curr: 1
                                    }
                                });
                            })

                        layer.close(index); //如果设定了yes回调，需进行手工关闭
                    }
                });
                break;
            case 'update':
                if (data.length === 0) {
                    layer.msg('请选择一行');
                } else if (data.length > 1) {
                    layer.msg('只能同时编辑一个');
                } else {
                    layer.alert('编辑 [id]：' + checkStatus.data[0].id);
                }
                break;
            case 'delete':
                if (data.length === 0) {
                    layer.msg('请选择一行');
                } else {
                    layer.msg('删除');
                }
                break;
        }
        ;
    });


    // 执行搜索，表格重载
    $('#do_search').on('click', function () {
        // 搜索条件
        var send_name = $('#send_name').val();
        var send_data = $('#send_data').val();
        table.reload('tableOne', {
            method: 'post'
            , where: {
                'token': token,
                'send_name': send_name,
                'send_data': send_data,
            }
            , page: {
                curr: 1
            }
        });
    });


    layer.msg('Hello World');
});






