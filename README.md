<!DOCTYPE html>
<html lang="en-US" class="theme-gitea">
<head>
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>project-configuration/README.md at master - project-configuration - Gitea: хостинг репозиториев исходных кодов</title>
	<link rel="manifest" href="data:application/json;base64,eyJuYW1lIjoiR2l0ZWE6INGF0L7RgdGC0LjQvdCzINGA0LXQv9C&#43;0LfQuNGC0L7RgNC40LXQsiDQuNGB0YXQvtC00L3Ri9GFINC60L7QtNC&#43;0LIiLCJzaG9ydF9uYW1lIjoiR2l0ZWE6INGF0L7RgdGC0LjQvdCzINGA0LXQv9C&#43;0LfQuNGC0L7RgNC40LXQsiDQuNGB0YXQvtC00L3Ri9GFINC60L7QtNC&#43;0LIiLCJzdGFydF91cmwiOiJodHRwczovL2dpdGVhLnJhZGl1bS5ncm91cC8iLCJpY29ucyI6W3sic3JjIjoiaHR0cHM6Ly9naXRlYS5yYWRpdW0uZ3JvdXAvYXNzZXRzL2ltZy9sb2dvLnBuZyIsInR5cGUiOiJpbWFnZS9wbmciLCJzaXplcyI6IjUxMng1MTIifSx7InNyYyI6Imh0dHBzOi8vZ2l0ZWEucmFkaXVtLmdyb3VwL2Fzc2V0cy9pbWcvbG9nby5zdmciLCJ0eXBlIjoiaW1hZ2Uvc3ZnK3htbCIsInNpemVzIjoiNTEyeDUxMiJ9XX0=">
	<meta name="author" content="radium">
	<meta name="description" content="project-configuration">
	<meta name="keywords" content="go,git,self-hosted,gitea">
	<meta name="referrer" content="no-referrer">


	<link rel="alternate" type="application/atom+xml" title="" href="/radium/project-configuration.atom">
	<link rel="alternate" type="application/rss+xml" title="" href="/radium/project-configuration.rss">

	<link rel="icon" href="/assets/img/favicon.svg" type="image/svg+xml">
	<link rel="alternate icon" href="/assets/img/favicon.png" type="image/png">
	
<script>
	window.addEventListener('error', function(e) {window._globalHandlerErrors=window._globalHandlerErrors||[]; window._globalHandlerErrors.push(e);});
	window.config = {
		appUrl: 'https:\/\/gitea.radium.group\/',
		appSubUrl: '',
		assetVersionEncoded: encodeURIComponent('1.20.4'), 
		assetUrlPrefix: '\/assets',
		runModeIsProd:  true ,
		customEmojis: {"codeberg":":codeberg:","git":":git:","gitea":":gitea:","github":":github:","gitlab":":gitlab:","gogs":":gogs:"},
		csrfToken: 'A_9LgQFbEc-ZmRQxTjq2aYrKIMo6MTcxMDY4ODA5MjMxNjk5MTg3Mw',
		pageData: {},
		notificationSettings: {"EventSourceUpdateTime":10000,"MaxTimeout":60000,"MinTimeout":10000,"TimeoutStep":10000}, 
		enableTimeTracking:  true ,
		
		mermaidMaxSourceCharacters:  5000 ,
		
		i18n: {
			copy_success: 'Copied!',
			copy_error: 'Copy failed',
			error_occurred: 'An error occurred',
			network_error: 'Network error',
			remove_label_str: 'Remove item \u0022%s\u0022',
		},
	};
	
	window.config.pageData = window.config.pageData || {};
</script>
<script src="/assets/js/webcomponents.js?v=1.20.4"></script>

	<noscript>
		<style>
			.dropdown:hover > .menu { display: block; }
			.ui.secondary.menu .dropdown.item > .menu { margin-top: 0; }
		</style>
	</noscript>

	
		<meta property="og:title" content="project-configuration">
		<meta property="og:url" content="https://gitea.radium.group/radium/project-configuration">
		
	
	<meta property="og:type" content="object">
	
		<meta property="og:image" content="https://gitea.radium.group/avatars/003ae0eb61359e1c9703b61947bb8067">
	

	<meta property="og:site_name" content="Gitea: хостинг репозиториев исходных кодов">
	<link rel="stylesheet" href="/assets/css/index.css?v=1.20.4">


	
<script type="text/javascript" >
   (function(m,e,t,r,i,k,a){m[i]=m[i]||function(){(m[i].a=m[i].a||[]).push(arguments)};
   m[i].l=1*new Date();k=e.createElement(t),a=e.getElementsByTagName(t)[0],k.async=1,k.src=r,a.parentNode.insertBefore(k,a)})
   (window, document, "script", "https://mc.yandex.ru/metrika/tag.js", "ym");

   ym(67941160, "init", {
        clickmap:true,
        trackLinks:true,
        accurateTrackBounce:true,
        webvisor:true
   });
</script>
<noscript><div><img src="https://mc.yandex.ru/watch/67941160" style="position:absolute; left:-9999px;" alt="" /></div></noscript>


</head>
<body>
	

	<div class="full height">
		<noscript>This website requires JavaScript.</noscript>

		

		
			


<nav id="navbar" class="ui secondary stackable menu" aria-label="Navigation Bar">
	<div class="item">
		
		<a href="/" aria-label="Home">
			<img width="30" height="30" src="/assets/img/logo.svg" alt="Logo" aria-hidden="true">
		</a>

		
		<div class="ui secondary menu navbar-mobile-right gt-gap-2">
			
			<button class="item ui icon mini button gt-p-3 gt-m-0" id="navbar-expand-toggle"><svg viewBox="0 0 16 16" class="svg octicon-three-bars" width="16" height="16" aria-hidden="true"><path d="M1 2.75A.75.75 0 0 1 1.75 2h12.5a.75.75 0 0 1 0 1.5H1.75A.75.75 0 0 1 1 2.75Zm0 5A.75.75 0 0 1 1.75 7h12.5a.75.75 0 0 1 0 1.5H1.75A.75.75 0 0 1 1 7.75ZM1.75 12h12.5a.75.75 0 0 1 0 1.5H1.75a.75.75 0 0 1 0-1.5Z"/></svg></button>
		</div>
	</div>

	
	
		<a class="item" href="/explore/repos">Explore</a>
	

	

	
		<a class="item" target="_blank" rel="noopener noreferrer" href="https://docs.gitea.com">Help</a>
	

	
	<div class="right menu">
		
			
			<a class="item" rel="nofollow" href="/user/login?redirect_to=%2fradium%2fproject-configuration%2f%2fsrc%2fbranch%2fmaster%2fREADME.md">
				<svg viewBox="0 0 16 16" class="svg octicon-sign-in" width="16" height="16" aria-hidden="true"><path d="M2 2.75C2 1.784 2.784 1 3.75 1h2.5a.75.75 0 0 1 0 1.5h-2.5a.25.25 0 0 0-.25.25v10.5c0 .138.112.25.25.25h2.5a.75.75 0 0 1 0 1.5h-2.5A1.75 1.75 0 0 1 2 13.25Zm6.56 4.5h5.69a.75.75 0 0 1 0 1.5H8.56l1.97 1.97a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L6.22 8.53a.75.75 0 0 1 0-1.06l3.25-3.25a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734Z"/></svg> Sign In
			</a>
		
	</div>
</nav>

		



<div role="main" aria-label="project-configuration/README.md at master" class="page-content repository file list ">
	<div class="header-wrapper">

	<div class="ui container">
		<div class="repo-header">
			<div class="repo-title-wrap gt-df gt-fc">
				<div class="repo-title" role="heading" aria-level="1">
					
					
						<div class="repo-icon gt-mr-3">
	
		
			<svg viewBox="0 0 16 16" class="svg octicon-repo" width="32" height="32" aria-hidden="true"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/></svg>
		
	
</div>

					
					<a href="/radium">radium</a>
					<div class="gt-mx-2">/</div>
					<a href="/radium/project-configuration">project-configuration</a>
					<div class="labels gt-df gt-ac gt-fw">
						
							
								
							
						
						
					</div>
					
						<a class="rss-icon gt-ml-3" href="/radium/project-configuration.rss" data-tooltip-content="RSS Feed"><svg viewBox="0 0 16 16" class="svg octicon-rss" width="18" height="18" aria-hidden="true"><path d="M2.002 2.725a.75.75 0 0 1 .797-.699C8.79 2.42 13.58 7.21 13.974 13.201a.75.75 0 0 1-1.497.098 10.502 10.502 0 0 0-9.776-9.776.747.747 0 0 1-.7-.798ZM2.84 7.05h-.002a7.002 7.002 0 0 1 6.113 6.111.75.75 0 0 1-1.49.178 5.503 5.503 0 0 0-4.8-4.8.75.75 0 0 1 .179-1.489ZM2 13a1 1 0 1 1 2 0 1 1 0 0 1-2 0Z"/></svg></a>
					
				</div>
				
				
				
			</div>
			
				<div class="repo-buttons">
					
					<form method="post" action="/radium/project-configuration/action/watch?redirect_to=%2fradium%2fproject-configuration%2f%2fsrc%2fbranch%2fmaster%2fREADME.md">
						<input type="hidden" name="_csrf" value="A_9LgQFbEc-ZmRQxTjq2aYrKIMo6MTcxMDY4ODA5MjMxNjk5MTg3Mw">
						<div class="ui labeled button" data-tooltip-content="Sign in to watch this repository.">
							<button type="submit" class="ui compact small basic button" disabled>
								<svg viewBox="0 0 16 16" class="svg octicon-eye" width="16" height="16" aria-hidden="true"><path d="M8 2c1.981 0 3.671.992 4.933 2.078 1.27 1.091 2.187 2.345 2.637 3.023a1.62 1.62 0 0 1 0 1.798c-.45.678-1.367 1.932-2.637 3.023C11.67 13.008 9.981 14 8 14c-1.981 0-3.671-.992-4.933-2.078C1.797 10.83.88 9.576.43 8.898a1.62 1.62 0 0 1 0-1.798c.45-.677 1.367-1.931 2.637-3.022C4.33 2.992 6.019 2 8 2ZM1.679 7.932a.12.12 0 0 0 0 .136c.411.622 1.241 1.75 2.366 2.717C5.176 11.758 6.527 12.5 8 12.5c1.473 0 2.825-.742 3.955-1.715 1.124-.967 1.954-2.096 2.366-2.717a.12.12 0 0 0 0-.136c-.412-.621-1.242-1.75-2.366-2.717C10.824 4.242 9.473 3.5 8 3.5c-1.473 0-2.825.742-3.955 1.715-1.124.967-1.954 2.096-2.366 2.717ZM8 10a2 2 0 1 1-.001-3.999A2 2 0 0 1 8 10Z"/></svg>Watch
							</button>
							<a class="ui basic label" href="/radium/project-configuration/watchers">
								1
							</a>
						</div>
					</form>
					
						<form method="post" action="/radium/project-configuration/action/star?redirect_to=%2fradium%2fproject-configuration%2f%2fsrc%2fbranch%2fmaster%2fREADME.md">
							<input type="hidden" name="_csrf" value="A_9LgQFbEc-ZmRQxTjq2aYrKIMo6MTcxMDY4ODA5MjMxNjk5MTg3Mw">
							<div class="ui labeled button" data-tooltip-content="Sign in to star this repository.">
								<button type="submit" class="ui compact small basic button" disabled>
									<svg viewBox="0 0 16 16" class="svg octicon-star" width="16" height="16" aria-hidden="true"><path d="M8 .25a.75.75 0 0 1 .673.418l1.882 3.815 4.21.612a.75.75 0 0 1 .416 1.279l-3.046 2.97.719 4.192a.751.751 0 0 1-1.088.791L8 12.347l-3.766 1.98a.75.75 0 0 1-1.088-.79l.72-4.194L.818 6.374a.75.75 0 0 1 .416-1.28l4.21-.611L7.327.668A.75.75 0 0 1 8 .25Zm0 2.445L6.615 5.5a.75.75 0 0 1-.564.41l-3.097.45 2.24 2.184a.75.75 0 0 1 .216.664l-.528 3.084 2.769-1.456a.75.75 0 0 1 .698 0l2.77 1.456-.53-3.084a.75.75 0 0 1 .216-.664l2.24-2.183-3.096-.45a.75.75 0 0 1-.564-.41L8 2.694Z"/></svg>Star
								</button>
								<a class="ui basic label" href="/radium/project-configuration/stars">
									0
								</a>
							</div>
						</form>
					
					
						<div class="ui labeled button
							
								disabled
							"
							
								data-tooltip-content="Sign in to fork this repository."
							
						>
							<a class="ui compact small basic button"
								
									
								
							>
								<svg viewBox="0 0 16 16" class="svg octicon-repo-forked" width="16" height="16" aria-hidden="true"><path d="M5 5.372v.878c0 .414.336.75.75.75h4.5a.75.75 0 0 0 .75-.75v-.878a2.25 2.25 0 1 1 1.5 0v.878a2.25 2.25 0 0 1-2.25 2.25h-1.5v2.128a2.251 2.251 0 1 1-1.5 0V8.5h-1.5A2.25 2.25 0 0 1 3.5 6.25v-.878a2.25 2.25 0 1 1 1.5 0ZM5 3.25a.75.75 0 1 0-1.5 0 .75.75 0 0 0 1.5 0Zm6.75.75a.75.75 0 1 0 0-1.5.75.75 0 0 0 0 1.5Zm-3 8.75a.75.75 0 1 0-1.5 0 .75.75 0 0 0 1.5 0Z"/></svg>Fork
							</a>
							<div class="ui small modal" id="fork-repo-modal">
								<div class="header">
									You&#39;ve already forked project-configuration
								</div>
								<div class="content gt-text-left">
									<div class="ui list">
										
									</div>
									
								</div>
							</div>
							<a class="ui basic label" href="/radium/project-configuration/forks">
								0
							</a>
						</div>
					
				</div>
			
		</div>
	</div>

	<div class="ui tabs container">
		
			<div class="ui tabular menu navbar gt-overflow-x-auto gt-overflow-y-hidden">
				
				<a class="active item" href="/radium/project-configuration">
					<svg viewBox="0 0 16 16" class="svg octicon-code" width="16" height="16" aria-hidden="true"><path d="m11.28 3.22 4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L13.94 8l-3.72-3.72a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215Zm-6.56 0a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L2.06 8l3.72 3.72a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L.47 8.53a.75.75 0 0 1 0-1.06Z"/></svg> Code
				</a>
				

				
					<a class="item" href="/radium/project-configuration/issues">
						<svg viewBox="0 0 16 16" class="svg octicon-issue-opened" width="16" height="16" aria-hidden="true"><path d="M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"/><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z"/></svg> Issues
						
							<span class="ui small label">1</span>
						
					</a>
				

				

				
					<a class="item" href="/radium/project-configuration/pulls">
						<svg viewBox="0 0 16 16" class="svg octicon-git-pull-request" width="16" height="16" aria-hidden="true"><path d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354ZM3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Z"/></svg> Pull Requests
						
					</a>
				

				

				

				
					<a href="/radium/project-configuration/projects" class="item">
						<svg viewBox="0 0 16 16" class="svg octicon-project" width="16" height="16" aria-hidden="true"><path d="M1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25V1.75C0 .784.784 0 1.75 0ZM1.5 1.75v12.5c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25V1.75a.25.25 0 0 0-.25-.25H1.75a.25.25 0 0 0-.25.25ZM11.75 3a.75.75 0 0 1 .75.75v7.5a.75.75 0 0 1-1.5 0v-7.5a.75.75 0 0 1 .75-.75Zm-8.25.75a.75.75 0 0 1 1.5 0v5.5a.75.75 0 0 1-1.5 0ZM8 3a.75.75 0 0 1 .75.75v3.5a.75.75 0 0 1-1.5 0v-3.5A.75.75 0 0 1 8 3Z"/></svg> Projects
						
					</a>
				

				
				<a class="item" href="/radium/project-configuration/releases">
					<svg viewBox="0 0 16 16" class="svg octicon-tag" width="16" height="16" aria-hidden="true"><path d="M1 7.775V2.75C1 1.784 1.784 1 2.75 1h5.025c.464 0 .91.184 1.238.513l6.25 6.25a1.75 1.75 0 0 1 0 2.474l-5.026 5.026a1.75 1.75 0 0 1-2.474 0l-6.25-6.25A1.752 1.752 0 0 1 1 7.775Zm1.5 0c0 .066.026.13.073.177l6.25 6.25a.25.25 0 0 0 .354 0l5.025-5.025a.25.25 0 0 0 0-.354l-6.25-6.25a.25.25 0 0 0-.177-.073H2.75a.25.25 0 0 0-.25.25ZM6 5a1 1 0 1 1 0 2 1 1 0 0 1 0-2Z"/></svg> Releases
					
				</a>
				

				
					<a class="item" href="/radium/project-configuration/wiki">
						<svg viewBox="0 0 16 16" class="svg octicon-book" width="16" height="16" aria-hidden="true"><path d="M0 1.75A.75.75 0 0 1 .75 1h4.253c1.227 0 2.317.59 3 1.501A3.743 3.743 0 0 1 11.006 1h4.245a.75.75 0 0 1 .75.75v10.5a.75.75 0 0 1-.75.75h-4.507a2.25 2.25 0 0 0-1.591.659l-.622.621a.75.75 0 0 1-1.06 0l-.622-.621A2.25 2.25 0 0 0 5.258 13H.75a.75.75 0 0 1-.75-.75Zm7.251 10.324.004-5.073-.002-2.253A2.25 2.25 0 0 0 5.003 2.5H1.5v9h3.757a3.75 3.75 0 0 1 1.994.574ZM8.755 4.75l-.004 7.322a3.752 3.752 0 0 1 1.992-.572H14.5v-9h-3.495a2.25 2.25 0 0 0-2.25 2.25Z"/></svg> Wiki
					</a>
				

				

				
					<a class="item" href="/radium/project-configuration/activity">
						<svg viewBox="0 0 16 16" class="svg octicon-pulse" width="16" height="16" aria-hidden="true"><path d="M6 2c.306 0 .582.187.696.471L10 10.731l1.304-3.26A.751.751 0 0 1 12 7h3.25a.75.75 0 0 1 0 1.5h-2.742l-1.812 4.528a.751.751 0 0 1-1.392 0L6 4.77 4.696 8.03A.75.75 0 0 1 4 8.5H.75a.75.75 0 0 1 0-1.5h2.742l1.812-4.529A.751.751 0 0 1 6 2Z"/></svg> Activity
					</a>
				

				

				
			</div>
		
	</div>
	<div class="ui tabs divider"></div>
</div>

	<div class="ui container ">
		




		
		
		
		

		<div class="repo-button-row">
			<div class="gt-df gt-ac gt-fw gt-gap-y-3">
				






	




<script type="module">
	const data = {
		'textReleaseCompare': "Compare",
		'textCreateTag': "Create tag \u003cstrong\u003e%s\u003c/strong\u003e",
		'textCreateBranch': "Create branch \u003cstrong\u003e%s\u003c/strong\u003e",
		'textCreateBranchFrom': "from \"%s\"",
		'textBranches': "Branches",
		'textTags': "Tags",

		'mode': 'branches',
		'showBranchesInDropdown':  true ,
		'searchFieldPlaceholder': 'Filter branch or tag...',
		'branchForm':  null ,
		'disableCreateBranch':  true ,
		'setAction':  null ,
		'submitForm':  null ,
		'viewType': "branch",
		'refName': "master",
		'commitIdShort': "26791c096a",
		'tagName': "",
		'branchName': "master",
		'noTag':  null ,
		'branches': ["master"],
		'tags': [],
		'defaultBranch': "master",
		'enableFeed':  true ,
		'rssURLPrefix': '\/radium\/project-configuration/rss/branch/',
		'branchURLPrefix': '\/radium\/project-configuration/src/branch/',
		'branchURLSuffix': '/README.md',
		'tagURLPrefix': '\/radium\/project-configuration/src/tag/',
		'tagURLSuffix': '/README.md',
		'repoLink': "/radium/project-configuration",
		'treePath': "README.md",
		'branchNameSubURL': "branch/master",
		'noResults': "No results found.",
	};
	
	window.config.pageData.branchDropdownDataList = window.config.pageData.branchDropdownDataList || [];
	window.config.pageData.branchDropdownDataList.push(data);
</script>

<div class="js-branch-tag-selector gt-mr-2">
	
	<div class="ui floating filter dropdown custom">
		<button class="branch-dropdown-button gt-ellipsis ui basic small compact button gt-df gt-m-0">
			<span class="text gt-df gt-ac gt-mr-2">
				
					
						<svg viewBox="0 0 16 16" class="svg octicon-git-branch" width="16" height="16" aria-hidden="true"><path d="M9.5 3.25a2.25 2.25 0 1 1 3 2.122V6A2.5 2.5 0 0 1 10 8.5H6a1 1 0 0 0-1 1v1.128a2.251 2.251 0 1 1-1.5 0V5.372a2.25 2.25 0 1 1 1.5 0v1.836A2.493 2.493 0 0 1 6 7h4a1 1 0 0 0 1-1v-.628A2.25 2.25 0 0 1 9.5 3.25Zm-6 0a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Zm8.25-.75a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5ZM4.25 12a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Z"/></svg>
					
					<strong ref="dropdownRefName" class="gt-ml-3">master</strong>
				
			</span>
			<svg viewBox="0 0 16 16" class="dropdown icon svg octicon-triangle-down" width="14" height="14" aria-hidden="true"><path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"/></svg>
		</button>
	</div>
</div>

				
					
					
					
					
					<a id="new-pull-request" role="button" class="ui compact basic button" href="/radium/project-configuration/compare/master...master"
						data-tooltip-content="Compare">
						<svg viewBox="0 0 16 16" class="svg octicon-git-pull-request" width="16" height="16" aria-hidden="true"><path d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354ZM3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Z"/></svg>
					</a>
				
				
				
				
				

				

				
				
					<span class="breadcrumb repo-path gt-ml-2">
						<a class="section" href="/radium/project-configuration/src/branch/master" title="project-configuration">project-configuration</a><span class="divider">/</span><span class="active section" title="README.md">README.md</span></span>
				
			</div>
			<div class="gt-df gt-ac">
				
				
				
			</div>
		</div>
		
			<div class="tab-size-8 non-diff-file-content">
	<h4 class="file-header ui top attached header gt-df gt-ac gt-sb gt-fw">
		<div class="file-header-left gt-df gt-ac gt-py-3 gt-pr-4">
			
				<div class="file-info text grey normal gt-mono">
	
	
	
		<div class="file-info-entry">
			473 B
		</div>
	
	
	
	
</div>

			
		</div>
		<div class="file-header-right file-actions gt-df gt-ac gt-fw">
			
				<div class="ui compact icon buttons two-toggle-buttons">
					<a href="/radium/project-configuration//src/branch/master/README.md?display=source" class="ui mini basic button " data-tooltip-content="View Source"><svg viewBox="0 0 16 16" class="svg octicon-code" width="15" height="15" aria-hidden="true"><path d="m11.28 3.22 4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L13.94 8l-3.72-3.72a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215Zm-6.56 0a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L2.06 8l3.72 3.72a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L.47 8.53a.75.75 0 0 1 0-1.06Z"/></svg></a>
					<a href="/radium/project-configuration//src/branch/master/README.md" class="ui mini basic button active" data-tooltip-content="View Rendered"><svg viewBox="0 0 16 16" class="svg octicon-file" width="15" height="15" aria-hidden="true"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"/></svg></a>
				</div>
			
			
				<div class="ui buttons gt-mr-2">
					<a class="ui mini basic button" href="/radium/project-configuration/raw/branch/master/README.md">Raw</a>
					
						<a class="ui mini basic button" href="/radium/project-configuration/src/commit/26791c096a89eb75fee0e22d0c651a0292d07b7a/README.md">Permalink</a>
					
					
						<a class="ui mini basic button" href="/radium/project-configuration/blame/branch/master/README.md">Blame</a>
					
					<a class="ui mini basic button" href="/radium/project-configuration/commits/branch/master/README.md">History</a>
					
				</div>
				<a download href="/radium/project-configuration/raw/branch/master/README.md"><span class="btn-octicon" data-tooltip-content="Download file"><svg viewBox="0 0 16 16" class="svg octicon-download" width="16" height="16" aria-hidden="true"><path d="M2.75 14A1.75 1.75 0 0 1 1 12.25v-2.5a.75.75 0 0 1 1.5 0v2.5c0 .138.112.25.25.25h10.5a.25.25 0 0 0 .25-.25v-2.5a.75.75 0 0 1 1.5 0v2.5A1.75 1.75 0 0 1 13.25 14Z"/><path d="M7.25 7.689V2a.75.75 0 0 1 1.5 0v5.689l1.97-1.969a.749.749 0 1 1 1.06 1.06l-3.25 3.25a.749.749 0 0 1-1.06 0L4.22 6.78a.749.749 0 1 1 1.06-1.06l1.97 1.969Z"/></svg></span></a>
				<a id="copy-content" class="btn-octicon " data-link="/radium/project-configuration/raw/branch/master/README.md" data-tooltip-content="Copy content"><svg viewBox="0 0 16 16" class="svg octicon-copy" width="14" height="14" aria-hidden="true"><path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"/><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"/></svg></a>
				
				<a class="btn-octicon" href="/radium/project-configuration/rss/branch/master/README.md"><svg viewBox="0 0 16 16" class="svg octicon-rss" width="14" height="14" aria-hidden="true"><path d="M2.002 2.725a.75.75 0 0 1 .797-.699C8.79 2.42 13.58 7.21 13.974 13.201a.75.75 0 0 1-1.497.098 10.502 10.502 0 0 0-9.776-9.776.747.747 0 0 1-.7-.798ZM2.84 7.05h-.002a7.002 7.002 0 0 1 6.113 6.111.75.75 0 0 1-1.49.178 5.503 5.503 0 0 0-4.8-4.8.75.75 0 0 1 .179-1.489ZM2 13a1 1 0 1 1 2 0 1 1 0 0 1-2 0Z"/></svg></a>
				
				
					
						<span class="btn-octicon disabled" data-tooltip-content="You must fork this repository to make or propose changes to this file."><svg viewBox="0 0 16 16" class="svg octicon-pencil" width="16" height="16" aria-hidden="true"><path d="M11.013 1.427a1.75 1.75 0 0 1 2.474 0l1.086 1.086a1.75 1.75 0 0 1 0 2.474l-8.61 8.61c-.21.21-.47.364-.756.445l-3.251.93a.75.75 0 0 1-.927-.928l.929-3.25c.081-.286.235-.547.445-.758l8.61-8.61Zm.176 4.823L9.75 4.81l-6.286 6.287a.253.253 0 0 0-.064.108l-.558 1.953 1.953-.558a.253.253 0 0 0 .108-.064Zm1.238-3.763a.25.25 0 0 0-.354 0L10.811 3.75l1.439 1.44 1.263-1.263a.25.25 0 0 0 0-.354Z"/></svg></span>
					
					
						<span class="btn-octicon disabled" data-tooltip-content="You must have write access to make or propose changes to this file."><svg viewBox="0 0 16 16" class="svg octicon-trash" width="16" height="16" aria-hidden="true"><path d="M11 1.75V3h2.25a.75.75 0 0 1 0 1.5H2.75a.75.75 0 0 1 0-1.5H5V1.75C5 .784 5.784 0 6.75 0h2.5C10.216 0 11 .784 11 1.75ZM4.496 6.675l.66 6.6a.25.25 0 0 0 .249.225h5.19a.25.25 0 0 0 .249-.225l.66-6.6a.75.75 0 0 1 1.492.149l-.66 6.6A1.748 1.748 0 0 1 10.595 15h-5.19a1.75 1.75 0 0 1-1.741-1.575l-.66-6.6a.75.75 0 1 1 1.492-.15ZM6.5 1.75V3h3V1.75a.25.25 0 0 0-.25-.25h-2.5a.25.25 0 0 0-.25.25Z"/></svg></span>
					
				
			
		</div>
	</h4>
	<div class="ui attached table unstackable segment">
		
		<div class="file-view markup markdown">
			
				<h1 id="user-content-project-configuration-stuff" dir="auto">Project Configuration Stuff</h1>
<h2 id="user-content-enforcing-configuration" dir="auto">Enforcing Configuration</h2>
<p dir="auto">Enforcing is done with the help of nitpick — a command-line tool.</p>
<h3 id="user-content-installation" dir="auto">Installation</h3>
<p dir="auto">Install nitpick:</p>
<pre class="code-block"><code class="chroma language-sh">pipx install nitpick
</code></pre><h3 id="user-content-usage" dir="auto">Usage</h3>
<p dir="auto">To check for errors only:</p>
<pre class="code-block"><code class="chroma language-sh">nitpick check
</code></pre><p dir="auto">To fix and modify your files directly:</p>
<pre class="code-block"><code class="chroma language-sh">nitpick fix
</code></pre><h2 id="user-content-initializing-a-project" dir="auto">Initializing a Project</h2>
<h3 id="user-content-python" dir="auto">Python</h3>
<pre class="code-block"><code class="chroma language-sh">cookiecutter https://gitea.radium.group/radium/project-configuration.git --directory cookiecutter-python
</code></pre>
			
		</div>
	</div>
</div>

		
	</div>
</div>


	

	</div>

	

	<footer class="page-footer" role="group" aria-label="Footer">
	<div class="left-links" role="contentinfo" aria-label="About Software">
		<a target="_blank" rel="noopener noreferrer" href="https://about.gitea.com">Powered by Gitea</a>
		
		
	</div>
	<div class="right-links" role="group" aria-label="Links">
		<div class="ui dropdown upward language">
			<span class="flex-text-inline"><svg viewBox="0 0 16 16" class="svg octicon-globe" width="14" height="14" aria-hidden="true"><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM5.78 8.75a9.64 9.64 0 0 0 1.363 4.177c.255.426.542.832.857 1.215.245-.296.551-.705.857-1.215A9.64 9.64 0 0 0 10.22 8.75Zm4.44-1.5a9.64 9.64 0 0 0-1.363-4.177c-.307-.51-.612-.919-.857-1.215a9.927 9.927 0 0 0-.857 1.215A9.64 9.64 0 0 0 5.78 7.25Zm-5.944 1.5H1.543a6.507 6.507 0 0 0 4.666 5.5c-.123-.181-.24-.365-.352-.552-.715-1.192-1.437-2.874-1.581-4.948Zm-2.733-1.5h2.733c.144-2.074.866-3.756 1.58-4.948.12-.197.237-.381.353-.552a6.507 6.507 0 0 0-4.666 5.5Zm10.181 1.5c-.144 2.074-.866 3.756-1.58 4.948-.12.197-.237.381-.353.552a6.507 6.507 0 0 0 4.666-5.5Zm2.733-1.5a6.507 6.507 0 0 0-4.666-5.5c.123.181.24.365.353.552.714 1.192 1.436 2.874 1.58 4.948Z"/></svg> English</span>
			<div class="menu language-menu">
				
					<a lang="de-DE" data-url="/?lang=de-DE" class="item ">Deutsch</a>
				
					<a lang="en-US" data-url="/?lang=en-US" class="item active selected">English</a>
				
					<a lang="es-ES" data-url="/?lang=es-ES" class="item ">español</a>
				
					<a lang="fr-FR" data-url="/?lang=fr-FR" class="item ">français</a>
				
					<a lang="it-IT" data-url="/?lang=it-IT" class="item ">italiano</a>
				
					<a lang="lv-LV" data-url="/?lang=lv-LV" class="item ">latviešu</a>
				
					<a lang="nl-NL" data-url="/?lang=nl-NL" class="item ">Nederlands</a>
				
					<a lang="pl-PL" data-url="/?lang=pl-PL" class="item ">polski</a>
				
					<a lang="pt-BR" data-url="/?lang=pt-BR" class="item ">português do Brasil</a>
				
					<a lang="fi-FI" data-url="/?lang=fi-FI" class="item ">suomi</a>
				
					<a lang="sv-SE" data-url="/?lang=sv-SE" class="item ">svenska</a>
				
					<a lang="tr-TR" data-url="/?lang=tr-TR" class="item ">Türkçe</a>
				
					<a lang="cs-CZ" data-url="/?lang=cs-CZ" class="item ">čeština</a>
				
					<a lang="bg-BG" data-url="/?lang=bg-BG" class="item ">български</a>
				
					<a lang="ru-RU" data-url="/?lang=ru-RU" class="item ">русский</a>
				
					<a lang="sr-SP" data-url="/?lang=sr-SP" class="item ">српски</a>
				
					<a lang="uk-UA" data-url="/?lang=uk-UA" class="item ">Українська</a>
				
					<a lang="ja-JP" data-url="/?lang=ja-JP" class="item ">日本語</a>
				
					<a lang="zh-CN" data-url="/?lang=zh-CN" class="item ">简体中文</a>
				
					<a lang="zh-TW" data-url="/?lang=zh-TW" class="item ">繁體中文（台灣）</a>
				
					<a lang="zh-HK" data-url="/?lang=zh-HK" class="item ">繁體中文（香港）</a>
				
					<a lang="ko-KR" data-url="/?lang=ko-KR" class="item ">한국어</a>
				
			</div>
		</div>
		<a href="/assets/js/licenses.txt">Licenses</a>
		<a href="/api/swagger">API</a>
		<a class="item" href="https://www.radium-it.ru/policy/">Privacy Policy</a>

	</div>
</footer>




	<script src="/assets/js/index.js?v=1.20.4" onerror="alert('Failed to load asset files from ' + this.src + '. Please make sure the asset files can be accessed.')"></script>

</body>
</html>

