<?php
namespace NethServer\Module\Arpwatch;
use Nethgui\System\PlatformInterface as Validate;

class ArpwatchService extends \Nethgui\Controller\AbstractController
{
    public function setDefaultValues($parameterName, $value)
    {
        $this->defaultValues[$parameterName] = $value;
        return $this;
    }
    public function initialize()
    {
    $this->declareParameter('status', Validate::SERVICESTATUS, array('configuration', 'arpwatch', 'status'));

    $this->declareParameter('arpmail', Validate::NOTEMPTY, array('configuration', 'arpwatch', 'email'));

    $this->declareParameter('interface', Validate::NOTEMPTY, array('configuration', 'arpwatch', 'interface'));

    $this->declareParameter('bogon', $this->createValidator()->memberOf('no','yes'), array('configuration', 'arpwatch', 'bogon'));

    $this->setDefaultValues('status', 'enabled');
    $this->setDefaultValues('bogon', 'no');
    parent::initialize();
    }


    public function onParametersSaved($changes)
    {
        $this->getPlatform()->signalEvent('nethserver-arpwatch-update@post-process');
    }
}
