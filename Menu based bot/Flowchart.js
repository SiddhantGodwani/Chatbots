"use strict";
(function($) {
  $.fn.flowchat = function(options) {
    // override options with user preferences
    var settings = $.extend({
      delay: 1500,
      startButtonId: '#btn-submit',
      autoStart: true,
      startMessageId: 1,
      dataJSON: null
    }, options);
    
    var container = $(this);
    
    // on click of Start button
    $(document).on('click', settings.startButtonId, function() {
      startChat(container, settings.dataJSON, settings.startMessageId, settings.delay)
    });
  }
  
  function selectOption($this, container, data, delay) {
    $this.parent().hide();
    var $userReply = $('<li class="user"><div class="text">' + $this.html() + '</div></li>');
    container.children('.chat-window').append($userReply);
    
    // get the message
    var nextMessageId = $this.attr('data-nextId');
    var nextMessage = findMessageInJsonById(data, nextMessageId);
    
    // add next message
    generateMessageHTML(container, data, nextMessage, delay);
  }
  
  function startChat(container, data, startId, delay) {
    // clear chat window
    container.html("<div class='footer-chat'>OpenGenus</div>");
    container.append("<ul class='chat-window'></ul>");
    
    // get the first message
    var message = findMessageInJsonById(data, startId);
    
    // add message
    generateMessageHTML(container, data, message, delay);
  }
  
  function findMessageInJsonById(data, id) {
    var messages = data;
    for (var i = 0; messages.length > i; i++)
      if (messages[i].id == id)
        return messages[i];
  }
  
  function addOptions(container, data, delay, m) {
    var $optionsContainer = $('<li class="options"></li>');
    var $optionsList = $('<ul></ul>');
    var optionText = null;
    var optionMessageId = null;
    for (var i = 1; i < 12; i++) {
      optionText = m["option" + i]
      optionMessageId = m["option" + i + "_nextMessageId"]
      if (optionText != "" && optionText != undefined && optionText != null) { // add option only if text exists
        var $optionElem = $("<li data-nextId=" + optionMessageId + ">" + optionText + "</li>");
        $optionElem.click(function() {
          selectOption($(this), container, data, delay)
        });
        $optionsList.append($optionElem);
      }
    }
    $optionsContainer.append($optionsList);
    return $optionsContainer;
  }
  
  function toggleLoader(status, container) {
    if (status == "show")
      container.children('.chat-window').append("<li class='typing-indicator'><span></span><span></span><span></span></li>");
    else
      container.find('.typing-indicator').remove();
  }
  
  function generateMessageHTML(container, messages, m, delay) {
    // create template if text is not null
    if (m.imageUrl != '')
      var $template = $('<li class')

      // Create chat icon
let d = document.createElement('div');
$(d).addClass('chat_icon')
    .html('<img src="src/icon.png" alt="" id="icon" style="position:fixed;bottom:0;right:0;height: 80px; width: 80px; float:right;">')
    .appendTo($("body")) //main div

// Add chat popup form to chat icon
$(".chat_icon").append(function() {
    return ($("<div>")
        .attr("id", "flowchat")
        .addClass("flow")
        .html('<div id="myForm" class="chat-popup"><form action="" class="form-container"><h3>OpenGenus</h3><input type="text" placeholder="Type Your Name" name="msg" required><button id="btn-submit" type="submit">Start</button></form></div>'))
});

// Toggle chat popup form visibility when chat icon is clicked
$(document).ready(function() {
    $('#icon').on('click', function() {
        if ($('.flow').is(':visible')) {
            $('.flow').fadeIn(400, function() {
                $('.flow').animate({
                    'width': 'hide'
                }, 1000);
            });
        } else {
            $('.flow').animate({
                'width': 'show'
            }, 1000, function() {
                $('.flow').fadeIn(400);
            });
        };
        if ($('.chat-popup').is(':visible')) {
            $('.chat-popup').fadeIn(400, function() {
                $('.chat-popup').animate({
                    'width': 'hide'
                }, 1000);
            });
        } else {
            $('.chat-popup').animate({
                'width': 'show'
            }, 1000, function() {
                $('.chat-popup').fadeIn(400);
            });
        };
    });
});

