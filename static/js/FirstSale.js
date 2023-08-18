document.addEventListener("DOMContentLoaded", function () {
    const categoryButtons = document.querySelectorAll(".category-button");
    const productContainers = document.querySelectorAll(".productGroup > div");

    let selectedGroups = []; // 선택된 그룹들을 저장할 배열

    categoryButtons.forEach(button => {
        button.addEventListener("click", function () {
            const clickedGroup = this.getAttribute("data-group");

            if (selectedGroups.includes(clickedGroup)) {
                // 이미 선택한 그룹 버튼을 누른 경우 선택을 해제하고 모든 품목 표시
                selectedGroups = selectedGroups.filter(group => group !== clickedGroup);

            } else {
                // 선택한 그룹 추가
                selectedGroups.push(clickedGroup);
            }

            if (selectedGroups.length === 0) {
                // 선택된 그룹이 없는 경우 모든 품목 표시
                productContainers.forEach(container => {
                    container.style.display = "block";
                });
            } else {
                // 선택한 그룹 품목 표시하며 나머지 숨김
                productContainers.forEach(container => {
                    if (selectedGroups.some(group => container.classList.contains(group))) {
                        container.style.display = "block";
                    } else {
                        container.style.display = "none";
                    }
                });

                // 선택한 그룹 품목들을 왼쪽 정렬하여 빈 공간 없이 나열
                let order = 1;
                productContainers.forEach(container => {
                    if (container.style.display === "block") {
                        container.style.order = order++;
                    }
                });
            }

            console.log(`Selected groups: ${selectedGroups}`);
            this.classList.toggle('aClick');// 선택한 그룹 확인을 위한 콘솔 출력
        });
    });

    // 선택해제 버튼 클릭 시 모든 품목 표시
    const deselectButton = document.querySelector(".category-button[data-group='resetList']");
    deselectButton.addEventListener("click", function () {
        selectedGroups = []; // 모든 선택 해제
        productContainers.forEach(container => {
            container.style.display = "block";
        });

        console.log(`Selected groups: ${selectedGroups}`); // 선택한 그룹 확인을 위한 콘솔 출력
    });
});
