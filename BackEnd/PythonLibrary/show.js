$(function() {
    $('#HighFieldset').hide();
    $('#LowFieldset').hide();
    $('#PostAutoPressure').hide();
});
function HighGoal() {
    $('#HighFieldset').show();
    $('#LowFieldset').hide();
}
function LowGoal() {
    $('#HighFieldset').hide();
    $('#LowFieldset').low();
}
function BothDisabled() {
    $('#HighFieldset').hide();
    $('#LowFieldset').hide();
}
function DisableAutoPressure() {
    $('#PostAutoPressure').hide();

}
function EnableAutoPressure() {
    $('#PostAutoPressure').show();
}