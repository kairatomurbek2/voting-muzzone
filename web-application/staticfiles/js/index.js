function checkVotePermissions() {
  $.post({
    url: '/check',
    success: function (data) {
      if (!data.success) {
        handleErrors(false, data.message);
        var time = data.message.match(/\d{1,2}/g);
        if (time && time.length >= 3) {
          $('.clock-wrap').css('display', 'inline-block');
          initClock(+time[0], +time[1], +time[2]);
        }
      }
    }
  })
}
function vote(event, questionId, choiceId) {
  event.preventDefault();
  $.post({
    url: '/' + questionId + '/vote',
    data: {
      choice: choiceId
    },
    success: function (data) {
      if(data.success) {
        $('#percent-' + data.id).text(data.percent + '%')
        handleErrors(true);
      } else {
        handleErrors(false, data.message);
      }
    }
  });
}

function handleErrors(success, message) {
  var defaultText = {
    success: 'Вы успешно проголосовали!',
    failure: 'Что-то пошло не так. Попробуйте позже'
  };
  var timeout = 2500;
  if (success) {
    if (message) {
      $('#alert-success').text(message).fadeIn('fast');
    } else {
      $('#alert-success').fadeIn('fast');
    }

    setTimeout(function () {
      $('#alert-success').fadeOut('fast').text(defaultText.success)
    }, timeout)
  }
  if (!success) {
    if (message) {
      $('#alert-danger').text(message).fadeIn('fast');
    } else {
      $('#alert-danger').fadeIn('fast');
    }
    setTimeout(function () {
      $('#alert-danger').fadeOut('fast').text(defaultText.failure)
    }, timeout)
  }
}

function initClock(h, min, sec) {
  var clock = $('#clock').FlipClock((h * 3600) + ((min * 60) + sec - 2)).setCountdown(true)
}

$(document).ready(function () {
  // checkVotePermissions();
  // initClock();
});