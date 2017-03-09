<!doctype html>
<html lang="en">
	<head>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
		<title>CORE 2062 Scouting</title>
		<link rel="shortcut icon" href="favicon.ico" />
		<meta name="description" content="CORE 2062 Scouting Form">
    	<meta name="author" content="CORE2062">
    	<meta name="robots" content="noindex, nofollow">

		<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/normalize/5.0.0/normalize.min.css" integrity="sha256-t2/7smZfgrST4FS1DT0bs/KotCM74XlcqZN5Vu7xlrw=" crossorigin="anonymous" />

		<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/foundation/5.5.3/css/foundation.min.css" integrity="sha256-NTds7atVCDeolLUzbcl45lx4gJYO+hNXCaX1wC2HQHc=" crossorigin="anonymous" />

		<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.1.1/jquery.min.js" integrity="sha256-hVVnYaiADRTO2PzUGmuLJr8BLUSjGIZsDYGmIJLv2b8=" crossorigin="anonymous"></script>

		<script src="https://cdnjs.cloudflare.com/ajax/libs/foundation/5.5.3/js/foundation.min.js" integrity="sha256-KXypdIy75PPHsbEaVkrhBvlQg8XTQy8NvalzrIxMrco=" crossorigin="anonymous"></script>

		<script src="https://cdnjs.cloudflare.com/ajax/libs/foundation/5.5.3/js/foundation/foundation.accordion.min.js" integrity="sha256-Sf8QyM10GIsdziOWIIfN7V/ah4iRxPt17tvNCHorXjc=" crossorigin="anonymous"></script>

		<script src="https://cdnjs.cloudflare.com/ajax/libs/foundation/5.5.3/js/foundation/foundation.tab.min.js" integrity="sha256-Qyd0HGGzEOB/qkGWHkxliFbXHCjs2VRDm8mzHEwphzk=" crossorigin="anonymous"></script>

		<script src="https://cdnjs.cloudflare.com/ajax/libs/awesomplete/1.1.1/awesomplete.min.js" integrity="sha256-hQ2PYbQiQS3xeguwt5BS+AMzn5V5JJ0P1kQnuoXdTnk=" crossorigin="anonymous"></script>

		<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/awesomplete/1.1.1/awesomplete.min.css" integrity="sha256-pMulKeKs7Hns5vhu0uluhawM68QSrKg/dFfttaXCKE8=" crossorigin="anonymous" />

		<script src="https://cdnjs.cloudflare.com/ajax/libs/parsley.js/2.6.2/parsley.min.js" integrity="sha256-QKOftzbqahZaXS2amOh27JacZ6TbmT4TmGxNo4Jue4Y=" crossorigin="anonymous"></script>

	</head>
	<body>

		<form name="main" id="form" action="add_to_database.php" method="post" data-parsley-validate>
			<div class="row">
				<div class="small-12 columns">
					<ul class="tabs show-for-medium-up" data-tab>
						<li class="tab-title active"><a href="#panel1">Match/Scout Info</a></li>
      					<li class="tab-title"><a href="#panel2">Autonomous Period</a></li>
      					<li class="tab-title"><a href="#panel3">Teleoperated Period</a></li>
      					<li class="tab-title"><a href="#panel4">Other</a></li>
      				</ul>
      				<dl class="accordion" data-accordion>
      					<dd class="accordion-navigation">
      					
      					<a href="#panel1" class="show-for-small-only">Match/Scout Info</a>
      						<div id="panel1" class="content active">
      							<div class="content-box section-box">
      								
      								<div class="row">
      									<div class="small-12 columns">
      										<label>Match Number: *
												<input name="MatchNumber" class="form-control" type="number" placeholder="1" value="<?php echo $_GET['match']; ?>" disabled/>
											</label>
										</div>
									</div>

									<div class="row">
										<div class="small-12 columns">
											<label>Team Number: *
												<input name="TeamNumber" class="form-control" value="<?php echo $_GET['team']; ?>" placeholder="2062" disabled/>
											</label>
										</div>
									</div>

									<div class="row">
										<div class="small-12 columns">
											<label>Scout Name: *
												<input name="ScoutName" class="awesomplete"  data-list="
												Brett,
												Draven,
												Noah
												" placeholder="John Smith" required/>
											</label>
										</div>
									</div>									

								</div>
							</div>

						<a href="#panel2" class="show-for-small-only">Autonomous Period</a>
	        				<div id="panel2" class="content">
	        					<div class="content-box section-box">

      								<div class="row">
      									<fieldset class="large-6 columns">
      										<legend>Deliver Gear:</legend>
      										 <input name="DeliverGearAuto" id="leftgear" value="LeftGearAuto" type="checkbox"><label for="leftgear">Left</label>
      										 <input name="DeliverGearAuto" id="middlegear" value="MiddleGearAuto" type="checkbox"><label for="middlegear">Middle</label>
      										 <input name="DeliverGearAuto" id="rightgear" value="RightGearAuto" type="checkbox"><label for="rightgear">Right</label>
      									</fieldset>
      								</div>

      								<div class="row">
      									<fieldset class="large-6 columns">
      										<legend>Crossed Baseline:</legend>
      										 <input id="CrossedBaseline" value="CrossedBaselineAuto" type="checkbox"><label for="CrossedBaseline">Yes</label>
      									</fieldset>
      								</div>

      								<div class="row">
      									<fieldset class="large-6 columns">
      										<legend>Score Fuel:</legend>
      										 <input name="FuelAuto" id="FuelLowAuto" value="FuelLowAuto" type="radio"><label for="FuelLowAuto">Low Goal</label>
      										 <input name="FuelAuto" id="FuelHighAuto" value="FuelHighAuto" type="radio"><label for="FuelHighAuto">High Goal</label>	 
      									</fieldset>
      								</div>

      								<div class="row">  <!--make this conditional based on fuel scoring in auto
      									<fieldset class="large-6 columns">-->
      										<legend>Pressure Quantity: *</legend>
      										<label>
      											<input type="tel" name="PressureAuto">
      										</label>
      									</fieldset>
      								</div>       								    									      						

								</div>
							</div>
							<input class="button round SubmitButton" type="submit" value="Submit"></input>	
							</form>
<script>
      $(document).foundation();
</script>
<script type="text/javascript">
  $('#form').parsley();
</script>

	</body>
</html>