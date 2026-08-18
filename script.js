/* ==========================================================================
   AI ENGINEERING STRATEGY — 3D INTERACTIVE PRESENTATION DECK ENGINE
   Includes Three.js WebGL 3D Scene Manager, Dynamic Mesh Animations, & Navigation
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
  // Navigation & UI Elements
  const slides = document.querySelectorAll('.slide');
  const totalSlides = slides.length;
  let currentSlide = 1;
  let autoplayTimer = null;
  let isAutoplay = false;

  const slideIndicator = document.getElementById('slideIndicator');
  const sectionBadge = document.getElementById('sectionBadge');
  const progressBar = document.getElementById('progressBar');
  const slideDots = document.getElementById('slideDots');
  const prevBtn = document.getElementById('prevBtn');
  const nextBtn = document.getElementById('nextBtn');
  const btnNotes = document.getElementById('btnNotes');
  const btnGrid = document.getElementById('btnGrid');
  const btnFullscreen = document.getElementById('btnFullscreen');
  const btnAutoplay = document.getElementById('btnAutoplay');
  const playIcon = document.getElementById('playIcon');
  const btnRestartDeck = document.getElementById('btnRestartDeck');

  const notesModal = document.getElementById('notesModal');
  const notesBody = document.getElementById('notesBody');
  const closeNotes = document.getElementById('closeNotes');

  const gridModal = document.getElementById('gridModal');
  const gridSlidesContainer = document.getElementById('gridSlidesContainer');
  const closeGrid = document.getElementById('closeGrid');

  // Presenter Notes Database
  const presenterNotes = {
    1: "Slide 1 (Title): Welcome leadership team. Today we present our comprehensive technical strategy comparing Machine Learning and Deep Learning models across automotive perception (driver behavior) and text NLP.",
    2: "Slide 2 (AI Foundations): Emphasize why static rule-based heuristics break down when facing raw high-dimensional telemetry or natural text, and how AI self-learns non-linear patterns.",
    3: "Slide 3 (Decision Matrix): Key slide for architectural defense. Highlight data modality (tabular vs unstructured), compute budgets (microcontrollers vs edge GPUs), and regulatory SHAP explainability.",
    4: "Slide 4 (ML Deep Dive): Walk through classical models. Highlight XGBoost for CAN-Bus telemetry risk scoring and Naive Bayes / SVM for fast text classification.",
    5: "Slide 5 (DL Deep Dive): Walk through deep vision (CNNs for cabin camera PERCLOS drowsiness), sequence LSTMs for time-series swerving, and BERT Transformers for bidirectional NLP context.",
    6: "Slide 6 (Driver Behavior): Detailed architecture breakdown. MobileNet-V3 CNN extracts eye aspect ratio (EAR) and hand phone poses, while Light XGBoost monitors CAN-Bus G-forces.",
    7: "Slide 7 (Text Classification): Compare classical TF-IDF + SVM (<1ms latency) against fine-tuned BERT (96.8% F1 accuracy) across customer support and toxic comment filtering.",
    8: "Slide 8 (Benchmarks & Maintenance): Show empirical validation curve progressing from 74% baseline ML up to 96.8% in our Two-Tier Cascade approach.",
    9: "Slide 9 (Deployment & Risks): Address concept drift (KS-statistics), silent model confidence drops, and edge TensorRT optimization on NVIDIA Jetson gateways.",
    10: "Slide 10 (Strategic Recommendation): Final pitch. Recommend the Two-Tier Hybrid Cascade approach (Tier 1 ML continuous screening + Tier 2 DL triggered perception), reducing compute cost by 65%."
  };

  // ==========================================================================
  // THREE.JS 3D ENGINE IMPLEMENTATION
  // ==========================================================================
  let scene, camera, renderer;
  let slide3DObjects = {};
  let mouseX = 0, mouseY = 0;
  let targetRotationX = 0, targetRotationY = 0;

  function init3DScene() {
    const canvas = document.getElementById('threeCanvas');
    if (!canvas || typeof THREE === 'undefined') return;

    // Scene & Camera setup
    scene = new THREE.Scene();
    camera = new THREE.PerspectiveCamera(60, window.innerWidth / window.innerHeight, 0.1, 1000);
    camera.position.z = 15;

    // Renderer setup
    renderer = new THREE.WebGLRenderer({ canvas: canvas, antialias: true, alpha: true });
    renderer.setSize(window.innerWidth, window.innerHeight);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

    // Ambient & Directional Lighting
    const ambientLight = new THREE.AmbientLight(0xffffff, 0.6);
    scene.add(ambientLight);

    const dirLight1 = new THREE.DirectionalLight(0x3b82f6, 1.2);
    dirLight1.position.set(10, 15, 10);
    scene.add(dirLight1);

    const dirLight2 = new THREE.DirectionalLight(0x8b5cf6, 1.0);
    dirLight2.position.set(-10, -10, -5);
    scene.add(dirLight2);

    // Build 3D Objects per Slide
    buildSlide3DObjects();

    // Mouse Tracking for Parallax
    document.addEventListener('mousemove', (e) => {
      mouseX = (e.clientX / window.innerWidth) * 2 - 1;
      mouseY = -(e.clientY / window.innerHeight) * 2 + 1;
    });

    window.addEventListener('resize', onWindowResize);

    // Start 3D Render Loop
    animate3D();
  }

  function buildSlide3DObjects() {
    // --------------------------------------------------------
    // SLIDE 1: Neural Lattice Sphere (Icosahedron + Core)
    // --------------------------------------------------------
    const group1 = new THREE.Group();
    const isoGeo = new THREE.IcosahedronGeometry(4, 2);
    const isoMat = new THREE.MeshStandardMaterial({
      color: 0x3b82f6,
      wireframe: true,
      emissive: 0x1d4ed8,
      emissiveIntensity: 0.5
    });
    const isoMesh = new THREE.Mesh(isoGeo, isoMat);
    group1.add(isoMesh);

    const coreGeo = new THREE.SphereGeometry(1.8, 32, 32);
    const coreMat = new THREE.MeshStandardMaterial({
      color: 0x8b5cf6,
      roughness: 0.2,
      metalness: 0.8,
      emissive: 0x6d28d9,
      emissiveIntensity: 0.6
    });
    const coreMesh = new THREE.Mesh(coreGeo, coreMat);
    group1.add(coreMesh);

    group1.position.set(0, 0, 0);
    scene.add(group1);
    slide3DObjects[1] = group1;

    // --------------------------------------------------------
    // SLIDE 2: Morphing Cube Lattice (AI Purpose)
    // --------------------------------------------------------
    const group2 = new THREE.Group();
    const cubeGeo = new THREE.BoxGeometry(4.5, 4.5, 4.5);
    const cubeMat = new THREE.MeshStandardMaterial({
      color: 0x10b981,
      wireframe: true,
      emissive: 0x059669,
      emissiveIntensity: 0.4
    });
    const cubeMesh = new THREE.Mesh(cubeGeo, cubeMat);
    group2.add(cubeMesh);

    const octGeo = new THREE.OctahedronGeometry(2.5);
    const octMat = new THREE.MeshStandardMaterial({
      color: 0x3b82f6,
      metalness: 0.9,
      roughness: 0.1
    });
    const octMesh = new THREE.Mesh(octGeo, octMat);
    group2.add(octMesh);

    group2.position.set(12, 0, 0); // Offset initially
    scene.add(group2);
    slide3DObjects[2] = group2;

    // --------------------------------------------------------
    // SLIDE 3: Torus Knot (ML vs DL)
    // --------------------------------------------------------
    const group3 = new THREE.Group();
    const tkGeo = new THREE.TorusKnotGeometry(3, 0.8, 128, 32);
    const tkMat = new THREE.MeshStandardMaterial({
      color: 0x8b5cf6,
      wireframe: true,
      emissive: 0x4c1d95,
      emissiveIntensity: 0.5
    });
    const tkMesh = new THREE.Mesh(tkGeo, tkMat);
    group3.add(tkMesh);

    group3.position.set(12, 0, 0);
    scene.add(group3);
    slide3DObjects[3] = group3;

    // --------------------------------------------------------
    // SLIDE 4: ML Scatter Cubes Grid
    // --------------------------------------------------------
    const group4 = new THREE.Group();
    for (let i = 0; i < 40; i++) {
      const boxGeo = new THREE.BoxGeometry(0.5, 0.5, 0.5);
      const boxMat = new THREE.MeshStandardMaterial({
        color: i % 2 === 0 ? 0x3b82f6 : 0xf59e0b,
        metalness: 0.5
      });
      const boxMesh = new THREE.Mesh(boxGeo, boxMat);
      boxMesh.position.set(
        (Math.random() - 0.5) * 10,
        (Math.random() - 0.5) * 8,
        (Math.random() - 0.5) * 8
      );
      group4.add(boxMesh);
    }
    group4.position.set(12, 0, 0);
    scene.add(group4);
    slide3DObjects[4] = group4;

    // --------------------------------------------------------
    // SLIDE 5: Deep Neural Network Planes
    // --------------------------------------------------------
    const group5 = new THREE.Group();
    for (let plane = -1; plane <= 1; plane++) {
      const planeGroup = new THREE.Group();
      planeGroup.position.x = plane * 3.5;
      for (let node = 0; node < 5; node++) {
        const nodeGeo = new THREE.SphereGeometry(0.4, 16, 16);
        const nodeMat = new THREE.MeshStandardMaterial({
          color: plane === 0 ? 0x8b5cf6 : 0x3b82f6,
          emissive: plane === 0 ? 0x6d28d9 : 0x1d4ed8,
          emissiveIntensity: 0.7
        });
        const nodeMesh = new THREE.Mesh(nodeGeo, nodeMat);
        nodeMesh.position.y = (node - 2) * 1.6;
        planeGroup.add(nodeMesh);
      }
      group5.add(planeGroup);
    }
    group5.position.set(12, 0, 0);
    scene.add(group5);
    slide3DObjects[5] = group5;

    // --------------------------------------------------------
    // SLIDE 6: 3D Automotive Wireframe Steering Ring
    // --------------------------------------------------------
    const group6 = new THREE.Group();
    const torusGeo = new THREE.TorusGeometry(3.5, 0.4, 16, 100);
    const torusMat = new THREE.MeshStandardMaterial({
      color: 0xef4444,
      wireframe: true,
      emissive: 0x991b1b,
      emissiveIntensity: 0.5
    });
    const torusMesh = new THREE.Mesh(torusGeo, torusMat);
    group6.add(torusMesh);

    group6.position.set(12, 0, 0);
    scene.add(group6);
    slide3DObjects[6] = group6;

    // --------------------------------------------------------
    // SLIDE 7: Floating Word Vector Cubes
    // --------------------------------------------------------
    const group7 = new THREE.Group();
    const ringGeo = new THREE.RingGeometry(2, 4.5, 32);
    const ringMat = new THREE.MeshStandardMaterial({
      color: 0x8b5cf6,
      side: THREE.DoubleSide,
      wireframe: true
    });
    const ringMesh = new THREE.Mesh(ringGeo, ringMat);
    group7.add(ringMesh);

    group7.position.set(12, 0, 0);
    scene.add(group7);
    slide3DObjects[7] = group7;

    // --------------------------------------------------------
    // SLIDE 8: 3D Industrial Turbine Rotor Ring
    // --------------------------------------------------------
    const group8 = new THREE.Group();
    const gearGeo = new THREE.CylinderGeometry(3.5, 3.5, 1, 16, 1, true);
    const gearMat = new THREE.MeshStandardMaterial({
      color: 0xf59e0b,
      wireframe: true,
      emissive: 0xb45309,
      emissiveIntensity: 0.5
    });
    const gearMesh = new THREE.Mesh(gearGeo, gearMat);
    group8.add(gearMesh);

    group8.position.set(12, 0, 0);
    scene.add(group8);
    slide3DObjects[8] = group8;

    // --------------------------------------------------------
    // SLIDE 9: 3D Edge Microchip Processor Box
    // --------------------------------------------------------
    const group9 = new THREE.Group();
    const chipGeo = new THREE.BoxGeometry(4, 0.4, 4);
    const chipMat = new THREE.MeshStandardMaterial({
      color: 0x10b981,
      metalness: 0.9,
      roughness: 0.1,
      emissive: 0x047857,
      emissiveIntensity: 0.5
    });
    const chipMesh = new THREE.Mesh(chipGeo, chipMat);
    group9.add(chipMesh);

    group9.position.set(12, 0, 0);
    scene.add(group9);
    slide3DObjects[9] = group9;

    // --------------------------------------------------------
    // SLIDE 10: Dual Cascading Concentric Rings
    // --------------------------------------------------------
    const group10 = new THREE.Group();
    const ring1Geo = new THREE.TorusGeometry(4, 0.2, 16, 100);
    const ring1Mat = new THREE.MeshStandardMaterial({ color: 0x3b82f6, emissive: 0x1d4ed8 });
    const ring1Mesh = new THREE.Mesh(ring1Geo, ring1Mat);

    const ring2Geo = new THREE.TorusGeometry(2.5, 0.2, 16, 100);
    const ring2Mat = new THREE.MeshStandardMaterial({ color: 0x8b5cf6, emissive: 0x6d28d9 });
    const ring2Mesh = new THREE.Mesh(ring2Geo, ring2Mat);

    group10.add(ring1Mesh);
    group10.add(ring2Mesh);

    group10.position.set(12, 0, 0);
    scene.add(group10);
    slide3DObjects[10] = group10;
  }

  function animate3D() {
    requestAnimationFrame(animate3D);

    // Smooth Mouse Parallax Tilt
    targetRotationY += (mouseX * 0.5 - targetRotationY) * 0.05;
    targetRotationX += (-mouseY * 0.5 - targetRotationX) * 0.05;

    camera.position.x = targetRotationY * 3;
    camera.position.y = targetRotationX * 3;
    camera.lookAt(0, 0, 0);

    // Animate and transition 3D objects based on current slide
    Object.keys(slide3DObjects).forEach(slideNum => {
      const obj = slide3DObjects[slideNum];
      if (!obj) return;

      const num = parseInt(slideNum, 10);
      if (num === currentSlide) {
        // Target active position (center background slightly right)
        obj.position.x += (2 - obj.position.x) * 0.08;
        obj.position.z += (0 - obj.position.z) * 0.08;
        obj.scale.x += (1 - obj.scale.x) * 0.08;
        obj.scale.y += (1 - obj.scale.y) * 0.08;
        obj.scale.z += (1 - obj.scale.z) * 0.08;

        // Rotation animation
        obj.rotation.x += 0.005;
        obj.rotation.y += 0.008;
      } else {
        // Hide inactive objects off to the side
        const offset = num < currentSlide ? -15 : 15;
        obj.position.x += (offset - obj.position.x) * 0.08;
        obj.scale.x += (0.001 - obj.scale.x) * 0.08;
        obj.scale.y += (0.001 - obj.scale.y) * 0.08;
        obj.scale.z += (0.001 - obj.scale.z) * 0.08;
      }
    });

    renderer.render(scene, camera);
  }

  function onWindowResize() {
    if (!camera || !renderer) return;
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
  }

  // ==========================================================================
  // SLIDE NAVIGATION & INTERACTION LOGIC
  // ==========================================================================

  function initDots() {
    slideDots.innerHTML = '';
    slides.forEach((_, idx) => {
      const dot = document.createElement('div');
      dot.classList.add('dot');
      if (idx === 0) dot.classList.add('active');
      dot.addEventListener('click', () => goToSlide(idx + 1));
      slideDots.appendChild(dot);
    });
  }

  function initGridModal() {
    gridSlidesContainer.innerHTML = '';
    slides.forEach((slide, idx) => {
      const slideNum = idx + 1;
      const section = slide.getAttribute('data-section') || `Slide ${slideNum}`;
      const titleEl = slide.querySelector('h1, h2');
      const titleText = titleEl ? titleEl.innerText.replace('\n', ' ') : `Slide ${slideNum}`;

      const thumb = document.createElement('div');
      thumb.classList.add('grid-thumb');
      thumb.innerHTML = `
        <div class="grid-thumb-num">SLIDE 0${slideNum} • ${section}</div>
        <div class="grid-thumb-title">${titleText}</div>
      `;
      thumb.addEventListener('click', () => {
        goToSlide(slideNum);
        gridModal.classList.remove('active');
      });
      gridSlidesContainer.appendChild(thumb);
    });
  }

  function goToSlide(slideNum) {
    if (slideNum < 1 || slideNum > totalSlides) return;

    slides.forEach(slide => slide.classList.remove('active'));
    currentSlide = slideNum;
    const targetSlide = document.querySelector(`.slide[data-slide="${currentSlide}"]`);
    
    if (targetSlide) {
      targetSlide.classList.add('active');
      
      slideIndicator.textContent = `SLIDE ${currentSlide.toString().padStart(2, '0')} / ${totalSlides.toString().padStart(2, '0')}`;
      const section = targetSlide.getAttribute('data-section') || 'EXECUTIVE OVERVIEW';
      sectionBadge.textContent = section;

      const progressPercent = (currentSlide / totalSlides) * 100;
      progressBar.style.width = `${progressPercent}%`;

      const dots = slideDots.querySelectorAll('.dot');
      dots.forEach((dot, idx) => {
        dot.classList.toggle('active', idx === currentSlide - 1);
      });

      if (notesBody) {
        notesBody.textContent = presenterNotes[currentSlide] || "No notes available for this slide.";
      }

      if (window.renderMathInElement) {
        window.renderMathInElement(targetSlide);
      }
    }
  }

  prevBtn.addEventListener('click', () => goToSlide(currentSlide - 1));
  nextBtn.addEventListener('click', () => goToSlide(currentSlide + 1));

  if (btnRestartDeck) {
    btnRestartDeck.addEventListener('click', () => goToSlide(1));
  }

  document.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'PageDown') {
      e.preventDefault();
      goToSlide(currentSlide + 1);
    } else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {
      e.preventDefault();
      goToSlide(currentSlide - 1);
    } else if (e.key === 'Home') {
      goToSlide(1);
    } else if (e.key === 'End') {
      goToSlide(totalSlides);
    } else if (e.key.toLowerCase() === 'f') {
      toggleFullscreen();
    } else if (e.key.toLowerCase() === 'n') {
      toggleNotesModal();
    } else if (e.key.toLowerCase() === 'g') {
      toggleGridModal();
    } else if (e.key === 'Escape') {
      notesModal.classList.remove('active');
      gridModal.classList.remove('active');
    }
  });

  function toggleFullscreen() {
    if (!document.fullscreenElement) {
      document.documentElement.requestFullscreen().catch(err => console.log(err));
    } else {
      if (document.exitFullscreen) {
        document.exitFullscreen();
      }
    }
  }

  btnFullscreen.addEventListener('click', toggleFullscreen);

  function toggleNotesModal() {
    notesModal.classList.toggle('active');
  }
  btnNotes.addEventListener('click', toggleNotesModal);
  closeNotes.addEventListener('click', () => notesModal.classList.remove('active'));

  function toggleGridModal() {
    gridModal.classList.toggle('active');
  }
  btnGrid.addEventListener('click', toggleGridModal);
  closeGrid.addEventListener('click', () => gridModal.classList.remove('active'));

  btnAutoplay.addEventListener('click', () => {
    isAutoplay = !isAutoplay;
    if (isAutoplay) {
      btnAutoplay.classList.add('active');
      playIcon.className = 'ph-bold ph-pause';
      autoplayTimer = setInterval(() => {
        if (currentSlide < totalSlides) {
          goToSlide(currentSlide + 1);
        } else {
          goToSlide(1);
        }
      }, 5000);
    } else {
      btnAutoplay.classList.remove('active');
      playIcon.className = 'ph-bold ph-play';
      clearInterval(autoplayTimer);
    }
  });

  function initTabSwitchers(containerId) {
    const container = document.getElementById(containerId);
    if (!container) return;

    const tabs = container.querySelectorAll('.algo-tab');
    tabs.forEach(tab => {
      tab.addEventListener('click', () => {
        tabs.forEach(t => t.classList.remove('active'));
        tab.classList.add('active');

        const targetId = tab.getAttribute('data-target');
        const parentSlide = container.closest('.slide-content');
        if (parentSlide) {
          const panels = parentSlide.querySelectorAll('.algo-panel');
          panels.forEach(panel => {
            if (panel.id === targetId) {
              panel.classList.add('active');
            } else {
              panel.classList.remove('active');
            }
          });
        }
      });
    });
  }

  // Initialize 3D Engine & Controls
  init3DScene();
  initDots();
  initGridModal();
  initTabSwitchers('mlTabs');
  initTabSwitchers('dlTabs');
  goToSlide(1);
});
