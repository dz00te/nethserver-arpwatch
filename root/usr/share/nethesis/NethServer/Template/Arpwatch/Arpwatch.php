?php
echo $view->header()->setAttribute('template', $T('ArpwatchService_Title'));
echo $view->panel()

#echo $view->fieldsetSwitch('status', 'enabled', $view::FIELDSETSWITCH_CHECKBOX)->setAttribute('uncheckedValue', 'disabled')

;
echo $view->buttonList($view::BUTTON_SUBMIT | $view::BUTTON_HELP);
?>

