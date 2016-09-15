<?php
echo $view->header()->setAttribute('template', $T('ArpwatchService_Title'));

echo $view->fieldsetSwitch('status', 'enabled', $view::FIELDSETSWITCH_CHECKBOX)->setAttribute('uncheckedValue', 'disabled')
    ->insert($view->textInput('arpmail'))
    ->insert($view->textInput('interface'))
    ->insert($view->checkbox('bogon', 'no')->setAttribute('uncheckedValue', 'yes'))
    ;
    echo $view->buttonList($view::BUTTON_SUBMIT | $view::BUTTON_HELP);
?>


