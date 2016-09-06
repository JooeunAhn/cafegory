$('#comments__new').click(function (e){
    e.preventDefault();
    $(this).addClass('disabled');
    var $form = $(this).closest('form');
    $.ajax({
        url: $(location).attr('href'),
        type: 'POST',
        data: {
            'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
            'message': $form.find('textarea[name="message"]').val(),
        },

        success: function(data){
            if (data){
                $('.comments').html(data);
            }
            else{
                console.error('데이터가 안넘어옴');
            }
        },
        error: function(xhr,errmsg,err){
            console.error(err);
        },
        complete: function() {
            $.getScript(js_root, function(){});
            $.getScript(customjs_root, function(){});
        }
    });
});

 /**
  * 댓글 수정하는 부분
  */
// 댓글 수정 클릭시 확장
$('.comment_edit').each(function (){
    $(this).click(function (){
        var $form = $(this).closest('.comments__item');
        $form.find('.form-group-upper:first').css('display', 'block');
        $form.find('.comments-item__content:first').css('display', 'none');
    });
});

// 수정 textarea 클릭 시 확장 js
$("textarea").each(function (){
    var first_time = true;
    $(this).on({
        focus: function() {
          if (first_time){
            $(this).data("original-height", $(this).outerHeight());
            first_time = false;
          }
          $(this).animate({ "height": "68px" }, 300);
        },
        blur: function() {
          if (!$(this).val()) {
            $(this).animate({ "height": $(this).data("original-height") }, 300);
            $(this).parents("form").find("button .comment_edit_submit").addClass("disabled");
          }
        },
        input: function() {
          $(this).parents("form").find("button .comment_edit_submit").removeClass("disabled");
        }
    });
});

// 수정 후 저장 클릭시 ajax 처리
$('.comment_edit_submit').each(function (){
    $(this).on('click', function (){
        var $form = $(this).closest('.comments__item').find('.edit-form');
        $.ajax({
            url: $form.attr('action'),
            type: 'POST',
            data: {
                'csrfmiddlewaretoken': $form.find('input[name=csrfmiddlewaretoken]').val(),
                'message': $form.find('textarea[name=message]').val(),
            },
            success: function(data){
                if (data){
                    $('.comments').html(data);
                }
                else{
                    console.error('데이터가 안넘어옴');
                }
            },
            error: function(xhr,errmsg,err){
                console.error(err);
            },
            complete: function() {
                $.getScript(js_root, function(){});
                $.getScript(customjs_root, function(){});
            }
        });
    });
});

// 수정 중 취소 클릭시 되돌아오게 하는 로직
$('.comment_edit_reset').each(function (){
    $(this).click(function (){
        var $form = $(this).closest('.comments__item');
        $form.find('.form-group-upper:first').css('display', 'none');
        $form.find('.comments-item__content:first').css('display', 'block');
    });
})
/**
 * 댓글 수정 끝
 */


/**
 * 댓글 삭제하는 로직
 */
$('.comment_del').each(function (){
    $(this).on('click', function (){
        if (confirm('삭제하시겠습니까?')) {
            var $form = $(this).closest('.comments__item').find('.del-form');
            $.ajax({
                url: $form.attr('action'),
                type: 'POST',
                data: {
                    'csrfmiddlewaretoken': $form.find('input[name=csrfmiddlewaretoken]').val(),
                },
                success: function(data){
                    if (data){
                        $('.comments').html(data);
                    }
                    else{
                        console.error('데이터가 안넘어옴');
                    }
                },
                error: function(xhr,errmsg,err){
                    console.error(err);
                },
                complete: function() {
                    $.getScript(js_root, function(){});
                    $.getScript(customjs_root, function(){});
                }
            });
        }
    });
});