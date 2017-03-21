$(function() {
    $('#HighFieldset').hide();
    $('#LowFieldset').hide();
    $('#PostAutoPressure').hide();
});
function HighGoal() {
    $('#HighFieldset').hide();
    $('#LowFieldset').show();
}
function LowGoal() {
    $('#HighFieldset').show();
    $('#LowFieldset').hide();
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