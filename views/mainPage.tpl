<html>
	<head>
		<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.4/jquery.min.js"></script>
		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css">
		<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
		<link rel="stylesheet" href="https://ajax.googleapis.com/ajax/libs/jqueryui/1.11.4/themes/smoothness/jquery-ui.css">
		<script src="https://ajax.googleapis.com/ajax/libs/jqueryui/1.11.4/jquery-ui.min.js"></script>
		<link rel="stylesheet" href="//netdna.bootstrapcdn.com/font-awesome/4.2.0/css/font-awesome.min.css">
		<link rel="stylesheet" type="text/css" href="static/style.css" />
	</head>

	<body>
	  <div class="page-header">
        <h1>Pastiche <small>Generate original poetry</small></h1>
      </div>
                <div class="panel-heading">Choose Your Inspiration:</div>
            <form method="post" action='/poetry_generator/'>
                <ul class="list-group" id="poets">
                    <li class="list-group-item">
                        Emily Dickinson
                        <div class="material-switch pull-right">
                            <input id="someSwitchOptionDefault" name="Dickinson" type="checkbox"/>
                            <label for="someSwitchOptionDefault" class="label-default"></label>
                        </div>
                    </li>
                    <li class="list-group-item">
                        Walt Whitman
                        <div class="material-switch pull-right">
                            <input id="someSwitchOptionPrimary" name="Whitman" type="checkbox"/>
                            <label for="someSwitchOptionPrimary" class="label-primary"></label>
                        </div>
                    </li>
                    <li class="list-group-item">
                        Shakespeare
                        <div class="material-switch pull-right">
                            <input id="someSwitchOptionSuccess" name="Shakespeare" type="checkbox"/>
                            <label for="someSwitchOptionSuccess" class="label-success"></label>
                        </div>
                    </li>
                    <li class="list-group-item">
                        Edgar Allan Poe
                        <div class="material-switch pull-right">
                            <input id="someSwitchOptionInfo" name="Poe" type="checkbox"/>
                            <label for="someSwitchOptionInfo" class="label-info"></label>
                        </div>
                    </li>
                    <li class="list-group-item">
                        E.E. Cummings
                        <div class="material-switch pull-right">
                            <input id="someSwitchOptionWarning" name="Cummings" type="checkbox"/>
                            <label for="someSwitchOptionWarning" class="label-warning"></label>
                        </div>
                    </li>
                    <li class="list-group-item">
                        Charles Bukowski
                        <div class="material-switch pull-right">
                            <input id="someSwitchOptionDanger" name="Bukowski" type="checkbox"/>
                            <label for="someSwitchOptionDanger" class="label-danger"></label>
                        </div>
                    </li>
                    <button type="submit" value="Submit" class="btn btn-primary">Compose</button>
                </ul>
        </form>
            <div class="form-group" id="output">
			  <label for="comment">Output:</label>
			  <textarea class="form-control" rows="5" id="comment">{{ poem }}</textarea>
			</div>
		
	</body>

    <script type="text/javascript">
    $(document).ready(function () {
        var arr = new Array();
        $('input[name="someSwitchOption001"]:checked').each(function () {
            arr.push(this.value);
            console.log(arr);
        });


    })
    </script>

</html>